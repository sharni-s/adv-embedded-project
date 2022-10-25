# Bridge program for testing UART receiver and Transmitter
import time
import serial

ser = serial.Serial(            
     port='/dev/serial0',
     baudrate = 115200,
     parity=serial.PARITY_NONE,
     stopbits=serial.STOPBITS_ONE,
     bytesize=serial.EIGHTBITS,
     timeout=2000
 )

# Sample data
# For future reference:
# A = set weight command, 
# 1 = TSLA, 
# AB = company news sentiment weight of 171,
# 55 = four candle hammer weight of 85, 
# 33 = bollinger bands weight of 51, 
# 21 = twitter message sentiment weight of 33, 
# C3 = relative strength index weight of 195
# Ref from: Self-Evolving Machine Learning Algorithm for Stock Market Trading Implemented on an FPGA

bytes_to_send = "A1AB553321C3" 

ser.write(bytes_to_send.encode())
bytes_received = ser.read(10)

print(bytes_received)