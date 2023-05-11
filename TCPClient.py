import socket

# define with server hostname or IP address
serverName = '' 

# define server port 
serverPort = 12000

# start socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input('Input word to be translated: ')
messageBytes = str.encode(message)

# send message to server
clientSocket.send(messageBytes)
# receive message from server
modifiedMessage = clientSocket.recv(1024)

# print received message
print("From Server:", modifiedMessage.decode())
#close client
clientSocket.close()