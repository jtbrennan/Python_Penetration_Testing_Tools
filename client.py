import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# This is an example IP, use the one you want
host = '192.168.0.23'
host = socket.gethostname()
port = 444

clientSocket.connect(('192.168.0.23', port))
#Max amount of data that can come from the port
message = clientSocket.recv(1024)
clientSocket.close()
print(message.decode('ascii'))
