import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname()
port = 444

# This is an example IP, use the one you want
serverSocket.bind(('192.168.0.23', port))
serverSocket.listen(3)

while True:
    clientSocket, address = serverSocket.accept()
    print("receive connection from" % str(address))
    message = 'Welcome, Thank you for Connecting to the Server' + "\r\n"
    clientSocket.send(message.encode('ascii'))

    clientSocket.close()
