import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1) #the USB port is ttyUSB0 this can change, the recommended baud rate is 57600

#these hexadecima code can be used with ser.write(). we use commandInventoryM, for more functions consult RT400_CommunicationsProtocol.pdf
commandInventoryM = "\xAA\x03\x11\x03\x55"		#Hex to query a single tag in loop mod
commandToSend = commandInventoryM #select the command to use

print("El puerto usado es: "+str(ser.name))
ser.write(commandToSend)
print("El comando hexadecimal enviado es: "+str(commandToSend.encode('hex')))

i = 0
numCont = 1
while i < 5:
	print("Leyendo ...")
	print("\n")
	rfidRead = ser.read(188)
	rfidReadSTR = str(rfidRead.encode('hex'))

	print("La respuesta es: "+rfidReadSTR+"\n")
	uii = rfidReadSTR.replace("55","\n")
	uii = uii.split()
	for x in uii:
		print("La UII del tag RFID numero "+str(numCont)+" es: "+x[8:]+"\n")
		numCont += 1

	ser.close()
	time.sleep(3)
	ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)
	ser.write(commandToSend)
	i += 1
	numCont = 1

ser.close()
print("Programa finalizado")
