import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1) #the USB port is ttyUSB0 this can change, the recommended baud rate is 57600

#these hexadecimal code can be used with ser.write(). we use commandInventoryS, for more functions consult RT400_CommunicationsProtocol.pdf
commandInventoryS = "\xAA\x02\x18\x55"			#Hex to query a single tag in single mode
commandToSend = commandInventoryS

print("El puerto usado es: "+str(ser.name))
ser.write(commandToSend)
print("El comando hexadecimal enviado es: "+str(commandToSend.encode('hex')))

i = 0
while i < 5:
	print("Leyendo ...")

	rfidRead = ser.read(50)
	rfidReadSTR = str(rfidRead.encode('hex'))
	print("\n")
	print("La respuesta es::"+rfidReadSTR)
	uii = rfidReadSTR.replace("55"," ")
	print("La UII de su tag RFID es:"+uii[8:]+"\n")

	ser.close()
	time.sleep(3)
	ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)
	ser.write(commandToSend)

	i += 1

ser.close()
print("Programa finalizado")
