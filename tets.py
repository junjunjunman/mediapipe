import serial
arduino= serial.Serial('COM8',9600)
while True :
    c=input()
    c=c.encode('utf-8')
    arduino.write(c)