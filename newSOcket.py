import socket
ip = '192.168.1.72'
port = 8010

cliente_socket = socket.socket()
cliente_socket.connect(ip, port)
print("Conectado al servidor.")

msj = input(" -> ")
while msj.lower().strip != 'cerrar':
    cliente_socket.send(msj.encode())
    data = cliente_socket.recv(1024).decode()

    print('Recivio server: '+ data)
    msj = input(' -> ')
    cliente_socket.close()