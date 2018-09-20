import serial
import serial.tools
#ser = serial.Serial('COM16', 9600, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
#print(ser.name)
#s = ser.read(100)

import serial

port = serial.Serial("COM16", baudrate=9600, timeout=3.0)

while True:
    port.write(b'\r\n0x00h')
    #.encode('utf-8')
    rcv = port.read(10)
    #port.write(b'\r\nYou sent:' + repr(rcv))
    #port.write(repr(rcv))
    print(rcv)
    
