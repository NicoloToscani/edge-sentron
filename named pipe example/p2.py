import os
import errno
import time

import sys

file_name = "/tmp/HmiRuntime"
mode = 0o777 # RW permisison
pipe = 0 
       
        
try:
    # File FIFO (named pipe) creation if doesn't exist
    os.mkfifo(file_name, mode)   
except OSError as oe: 
    if oe.errno != errno.EEXIST:
       raise
    elif(oe.errno == errno.EEXIST):
       print("File already exist")

while(True):       
     f = os.open(file_name, os.O_RDWR|os.O_CREAT)
     len_bytes = sys.getsizeof(f)
     print(len_bytes)
     read_value = os.read(f, len_bytes) 
     app = read_value.decode('UTF-8')
     print(read_value)
     os.close(pipe)
     
     '''
     # Scrivo per leggere altro lato
     print("Call write and wait")
     pipe = os.open(file_name, os.O_RDWR|os.O_CREAT)
     print("Scrivo")
     write_value = ('Ti sto scrivendo dal processo 2')
     s = write_value.encode('UTF-8')
     print(s)
     os.write(pipe,s)
     os.close(pipe)
     '''
     time.sleep(8)
     
