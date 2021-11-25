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
       
f = open(file_name, 'r')
read_value = f.read();
print(read_value)
         
