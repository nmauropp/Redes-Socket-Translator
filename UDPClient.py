import socket
# define with server hostname or IP address
serverName = 'LAPTOP-V26F8B6E' 

# define server port 
serverPort = 12000 

# start socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input('Input portuguese word:')

messageBytes = message.encode()


# send message to server
clientSocket.sendto(messageBytes, (serverName, serverPort))
# receive message from server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# print received message
print(modifiedMessage.decode())
# close client
clientSocket.close()
