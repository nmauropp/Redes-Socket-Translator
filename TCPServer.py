import socket

translator = {
    'atraso': 'delay',
    'comutador': 'switch',
    'enlace': 'link',
    'fio': 'wire',
    'hospedeiro': 'host',
    'mensagem': 'message',
    'rede': 'network',
    'roteador': 'router',
    'servidor': 'server',
    'transmissão': 'transmission'
}

# define port
serverPort = 12000

# start socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024).decode()
    if message in translator:
        translation = translator[message]
        connectionSocket.send(translation.encode())
    else:
        connectionSocket.send('Word could not be found in dictionary'.encode())
    connectionSocket.close()