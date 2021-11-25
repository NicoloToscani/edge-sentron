import os
import errno
import time

file_name = "/tmp/HmiRuntime"
mode = 0o600 # RW permisison
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
         
         f = open(file_name, 'w')
         print("Scrivo")
         # read_data = f.read()
         write_value = ('sono il produttore')
         s = str(write_value)
         f.write(s)
         
         print("Scritto su pipe")
         f.close()
         time.sleep(5)
   







