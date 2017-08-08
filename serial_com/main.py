import serial
com_port = input('Enter Com port: ')
ser =serial.Serial()
ser.baudrate = 19200
ser.port =com_port
ser.open()
ser.write('INNO1')
ser.close
