import serial

port=input('Enter port number:')
comport=serial.Serial(port)
comport.baudrate=9600
comport.bytesize=6
comport.parity='N'
comport.stopbits=1
data=bytearray(b'A')
No=comport.write(data)
comport.close()


