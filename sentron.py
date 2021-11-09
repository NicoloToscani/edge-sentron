from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from datetime import datetime
from enum import Enum
import time
import numpy as np

# Define connection state
#class ConnectionState(Enum):
    # OFFLINE = 0
    # ONLINE = 1

# Connection state init
connection_state = 0

# To do
plc_address = 192.168.100.3
modbus_port = 502
port_number = 1
    
print(f'PLC_ADDRESS= {plc_address}')
print(f'MODBUS_PORT= {modbus_port}')
print(f'DATABASE_NAME= {database_name}')
print(f'PORT_NUMBER= {port_number}')
print(f'DATABASE_NUMBER= {database_number}')
        
# Values array - Matrix 100 INT   
values = np.zeros(100)

#DValues array
dvalues = np.zeros(5)

# Modbus client
client = ModbusClient(plc_address, modbus_port)

# Try first socket connection
connection_state = client.connect()

# Error code 
error_code = 0
error_code_desc = ""

try:
 if(connection_state == True):
    connection_state = 1
    print("PLC connection: ONLINE")
 elif(connection_state == False):
    connection_state = 0
    print("PLC connection: OFFLINE")
except:
    connection_state = 0
    print("PLC connection: OFFLINE")
   
#Read register each 5s

while True:
  
   # Start reading time
   startime = time.time()

   print("------------------------------------")
   timestamp = datetime.now()   
   print("Timestamp: ", timestamp)
   if(connection_state == 1):
        print("Connection state: ONLINE")
   elif(connection_state == 0):
        print("Connection state: OFFLINE")
  

   # If connection is open run modbus reading registers
   if(connection_state == 1):
    
      try: 
              # Read 50 registers - 16 int
              register = 1000 # start address
              request = client.read_holding_registers(register, 100, unit = 1)
              
              # print(request.registers)
              
              # decode_16_bit
              index_register = 0
              index_register_modbus = 0
              
              for index_register in range (50):
              
                  
                  temp_register_value_1 = request.registers[index_register_modbus]
                  temp_register_value_2 = request.registers[index_register_modbus + 1]
                  temp_registers = []
                  temp_registers.append(temp_register_value_1)
                  temp_registers.append(temp_register_value_2)
                  
                  decoder = BinaryPayloadDecoder.fromRegisters(temp_registers, Endian.Big, wordorder=Endian.Big)
                  values[index_register] = decoder.decode_16bit_int()
                  
                  index_register_modbus += 2
                  
                  
                  
                  
              # print(index_register_modbus)    
              # Read 50 registers - DINT and SET
              register = 1050 # start address
              request = client.read_holding_registers(register, 100, unit = 1)
              
              # print(request.registers)
              
              # decode_32_bit
              index_register = 0
              index_register_modbus = 0
              d_value_index = 0
               
              # DINT values 
              for index_register in range (5):
              
                  temp_register_value_1 = request.registers[index_register_modbus]
                  temp_register_value_2 = request.registers[index_register_modbus + 1]
                  temp_register_value_3 = request.registers[index_register_modbus + 2]
                  temp_register_value_4 = request.registers[index_register_modbus + 3]
                  
                  temp_registers = []
                  temp_registers.append(temp_register_value_1)
                  temp_registers.append(temp_register_value_2)
                  temp_registers.append(temp_register_value_3)
                  temp_registers.append(temp_register_value_4)
                  
                  decoder = BinaryPayloadDecoder.fromRegisters(temp_registers, Endian.Big, wordorder=Endian.Little)
                  dvalues[d_value_index] = decoder.decode_32bit_int()
                  
                  
                  # d_values index increment
                  d_value_index += 1
                  
                  # for index increment
                  index_register_modbus += 4
                  
                  # print(index_register)
                  
              # print(index_register_modbus) 
                  
              
              # decode_16_bit
              index_register = 0
              index_register_modbus = 20
              
              for index_register in range (40):
              
                  
                  temp_register_value_1 = request.registers[index_register_modbus]
                  temp_register_value_2 = request.registers[index_register_modbus + 1]
                  temp_registers = []
                  temp_registers.append(temp_register_value_1)
                  temp_registers.append(temp_register_value_2)
                  
                  decoder = BinaryPayloadDecoder.fromRegisters(temp_registers, Endian.Big, wordorder=Endian.Big)
                  values[index_register + 60] = decoder.decode_16bit_int()
                  
                  index_register_modbus += 2
                  
              
               
               
               
      except  Exception as e:
              values = np.zeros(100)
              error_code = 1
              error_code_desc = e.args[0]
              # client.close()
              connection_state = 0
              # break

      # End time
      endtime = time.time()
      print("Execution time: %s seconds " % (endtime - startime))
      print("Error code: ", error_code, " description: ", error_code_desc)
      time.sleep(5)
     
     
   # Else if connection is close store zeros in to dabatabase
   elif(connection_state == 0):
      
        values = np.zeros(100)
        dvalues = np.zeros(5)
                
        # End time
        endtime = time.time()
        print("Execution time: %s seconds " % (endtime - startime))
        #  print("Error: ", error_code)
        print("Error code: ", error_code, " description: ", error_code_desc)
        connection_state = client.connect()
     
        if(connection_state == True):
           connection_state = 1
           # print("Re-Connection: ", connection_state)
           error_code = 0
           error_code_desc = ""
        elif(connection_state == False):
           connection_state = 0
           # print("Re-Connection: ", connection_state)
           error_code = 0
           error_code_desc = ""

        time.sleep(5)



