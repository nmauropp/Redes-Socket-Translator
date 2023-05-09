from socket import *
# define port
serverPort = 12000
# start socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# links socket to address
serverSocket.bind(('', serverPort))

# Words that can be translated
translate = {
    'servidor': 'server',
    'atraso':'delay',
    'enlace': 'link',
    'mensagem': 'message',
    'rede': 'network',
    'comutador': 'switch',
    'hospedeiro': 'host',
    'fio': 'wire',
    'transmissão': 'transmission',
    'roteador': 'router'
}

print("The server is ready to receive")

while(True):
        message, clientAddress = serverSocket.recvfrom(2048)
        
        receivedMessage = message.decode()
        
        if receivedMessage in translate:
                englishWord = translate[receivedMessage]
        else:
                englishWord = 'Error: Word not found.'

        response = englishWord.encode()
        serverSocket.sendto(response, clientAddress)