import serial
import Innowptx


print("Enter your Comport below")

ser = serial.Serial()
comport = input("Enter your comport: ")
ser.port = comport
ser.baudrate=9600
ser.parity=serial.PARITY_NONE
ser.stopbits=serial.STOPBITS_ONE
ser.bytesize=serial.EIGHTBITS
ser.open()
if ser.isOpen():
    print ("Serial port opened")
    Innowptx.Select_options()
else:
    print("!!!Cannot open serial port!!!\n\r\n\r")
    exit()