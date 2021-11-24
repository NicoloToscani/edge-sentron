import io
import os
# import msvcrt as ms # for fd magic
# import win32api, win32file, win32pipe
import struct
import traceback
import errno


class ODK_pipe(io.IOBase):

    def __init__(self, name,
                 outbuffersize=1000000,inbuffersize=1000000):
        """ An implementation of a file-like Python object pipe.

        Documentation can be found at
        https://msdn.microsoft.com/en-us/library/windows/desktop/aa365150(v=vs.85).aspx

        """
        self.name = name
        self.outbuffersize = outbuffersize
        self.inbuffersize = inbuffersize
        # Create pipe
        self.file_name = "/tmp/HmiRuntime"
        self.mode = 0o600 # TODO check permisisions for read/write 
        self.pipe = 0 
       
        
        try:
             os.mkfifo(self.file_name, self.mode)  
        except OSError as oe: 
            if oe.errno != errno.EEXIST:
               raise
        
    def __del__(self):
        try:
            self.pipe = os.open(self.file_name, os.O_RDWR|os.O_CREAT)
            os.write(self.pipe, ''.encode())
        except Exception:
           traceback.print_exc() 
        os.close(self.pipe)

    def __exit__(file):
        os.remove(file)

    # Use docstrings, not comments
    def isatty(self):
        """Is the stream interactive (connected to a terminal/tty)?"""
        return False

    def seekable(self):
        return False

    def fileno(self):
        # return self.fd
        raise NotImplementedError

    def seek(self):
        # I think this is clearer than an IOError
        raise NotImplementedError

    def tell(self):
        # as above
        raise NotImplementedError

    def isDataInPipe(self):
        try:
            # Cehck if buffer is not empty
            data_buffer = os.path.getsize(self.pipe)
            if data_buffer != 0:
               finished = 1
        except Exception:
           traceback.print_exc() 
        return data_buffer

    def readPipeBuffer(self):
        finished = 0
        fullDataRead = []

        while 1:
            try:
                bytesToRead = os.path.getsize(self.pipe)
                finished = 0
                if not bytesToRead:
                    break
                # Read pipe  
                data = os.read(self.pipe,bytesToRead)  
                fullDataRead.append(data)
            except Exception:
                traceback.print_exc() 
                break

        dataBuf = ''.join(fullDataRead)
        return dataBuf

    def write(self, data):
        """WriteFileEx impossible due to callback issues."""
        # there is no need to compare the __name__ of the type!
        #data = data + "\r\n"
        if not isinstance(data, bytes):
            data = bytes(data, 'utf-8')
        res = os.write(self.pipe, data)
        return len(data)

    def close(self):
        try:
            if self.handle:
                os.close(self.pipe)
            self.pipe = 0
        except Exception:
            pass

    def read(self, length=None):
        # Always compare None by identity, not equality
        if length is None:
            length = self.inbuffersize
        resp = os.read(self.pipe,length) 
        if resp[0] != 0:
            # TODO ?????
            #raise __builtins__.BrokenPipeError(win32api.FormatMessage(resp[0]))
            print(resp[0])
        else:
            return resp[1]
           
