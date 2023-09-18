#import socket module 
from socket import * 
import sys # In order to terminate the program 

IP    = 'localhost'
PORTA = 6789

serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a sever socket 
serverSocket.bind((IP, PORTA))
serverSocket.listen()

while True: 
    #Establish the connection
    print('Pronto para servir... ')
    connectionSocket, addr = serverSocket.accept()

    try:
        print('Aguardando login')
        message = connectionSocket.recv(6000)
        message_parts = message.split()

        if len(message_parts) >= 2:
            filename = message_parts[1]
            f = open(filename[1:], 'rb')
            outputdata = f.read()

            # Send HTTP response header
            response_header = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: ' + str(
                len(outputdata)).encode() + b'\r\n\r\n'
            connectionSocket.send(response_header)

            # Send the content of the requested file to the client
            print('Enviando mensagem')
            connectionSocket.send(outputdata)
            connectionSocket.close()
            print('Mensagem enviada')
        else:
            raise IOError


    except IOError:
        #Send response message for file not found
        errorMessage = b'HTTP/1.1 404 Not Found\r\n\r\nArquivo nao encontrado'
        connectionSocket.send(errorMessage)

        #Close client socket
        connectionSocket.close()

    #sys.exit()#Terminate the program after sending the corresponding data