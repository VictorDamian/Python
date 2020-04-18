import socket

ip = '192.168.1.72'
puerto = 8010

miSock = socket.socket()
miSock.connect((ip,puerto))

print("conectado al server")

while True:
	msj = raw_input ("Mensaje >> ")
	miSock.send(msj)
miSock.close()
print("Conn closed")