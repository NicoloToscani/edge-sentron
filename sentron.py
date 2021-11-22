from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from datetime import datetime
from enum import Enum
import time
import numpy as np

# Set WinCC Unified values
def setValues(values):
    # HMI variables
    voltage-L1N = values[0]

  

# Polling time (s)
polling_time = 5

# Connection state init
connection_state = 0

# Modbus TCP parameters
plc_address = "192.160..100.3"
modbus_port = 502
unit_id = 1

# Modbus TCP/IP enable
modbus_enable = 0
        
# Values array - Device registers - Create device class 
values = np.zeros(150)

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
   

#Read register - Set interval from HMI

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
              register_1 = 1 # start address first block
              request_1 = client.read_holding_registers(register_1, 100, unit_id = 1)

              # Read 50 registers - 16 int
              register_2 = 50 # start address second block
              request_2 = client.read_holding_registers(register_2, 100, unit_id = 1)

              # Read 50 registers - 16 int
              register_3 = 549 # start address third block
              request_3 = client.read_holding_registers(register_3, 100, unit_id = 1)
              
              # decode_16_bit
              index_register = 0
              index_register_modbus = 0
              
              # Compose 1 to 41 index register
              for index_register in range (50):
              
                  temp_register_value_1 = request_1.registers[index_register_modbus]
                  temp_register_value_2 = request.registers[index_register_modbus + 1]
                  temp_registers = []
                  temp_registers.append(temp_register_value_1)
                  temp_registers.append(temp_register_value_2)
                  
                  decoder = BinaryPayloadDecoder.fromRegisters(temp_registers, Endian.Big, wordorder=Endian.Big)
                  values[index_register] = decoder.decode_16bit_int()
                  
                  index_register_modbus += 2

              # decode_16_bit
              index_register = 50
              index_register_modbus = 0

              # Compose 55 to 71 index register
              for index_register in range (50):
              
                  temp_register_value_1 = request_2.registers[index_register_modbus]
                  temp_register_value_2 = request.registers[index_register_modbus + 1]
                  temp_registers = []
                  temp_registers.append(temp_register_value_1)
                  temp_registers.append(temp_register_value_2)
                  
                  decoder = BinaryPayloadDecoder.fromRegisters(temp_registers, Endian.Big, wordorder=Endian.Big)
                  values[index_register] = decoder.decode_16bit_int()
                  
                  index_register_modbus += 2
               # decode_16_bit
              index_register = 100
              index_register_modbus = 0

              # Compose 549 to 559 index register
              for index_register in range (50):
              
                  temp_register_value_1 = request_2.registers[index_register_modbus]
                  temp_register_value_2 = request.registers[index_register_modbus + 1]
                  temp_registers = []
                  temp_registers.append(temp_register_value_1)
                  temp_registers.append(temp_register_value_2)
                  
                  decoder = BinaryPayloadDecoder.fromRegisters(temp_registers, Endian.Big, wordorder=Endian.Big)
                  values[index_register] = decoder.decode_16bit_int()
                  
                  index_register_modbus += 2
              
      except  Exception as e:
              values = np.zeros(150)
              error_code = 1
              error_code_desc = e.args[0]
              # client.close()
              connection_state = 0
              # break
        
      # Write on WinCC 
      setValues(values)

      # End time
      endtime = time.time()
      print("Execution time: %s seconds " % (endtime - startime))
      print("Error code: ", error_code, " description: ", error_code_desc)
      time.sleep(polling_time)
     
     
   # Else if connection is close store zeros in to dabatabase
   elif(connection_state == 0):
      
        values = np.zeros(150)

        # Write zeros on WinCC 
        setValues(values)

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

        time.sleep(polling_time)
