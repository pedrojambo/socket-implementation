#import socket module 
from socket import * 
import sys # In order to terminate the program 

IP    = 'localhost'
PORTA = 6789

serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a sever socket 
serverSocket.bind((IP, PORTA))
serverSocket.listen(1)

while True: 
    #Establish the connection
    print('Pronto para servir... ')
    connectionSocket, addr = serverSocket.accept()
  
    #Get request
    message  = connectionSocket.recv(1024).decode("UTF-8")
    
    if message.startswith("GET"):
        try:
            print('Procurando arquivo')
            filename = message.split()[1]
            f = open(filename[1:], 'rb')
            outputdata = f.read()
            f.close()

            #Send one HTTP header line into socket
            header = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: ' + str(len(outputdata)).encode() + b'\r\n\r\n'
            connectionSocket.send(header)
            
            #Send the content of the requested file to the client 
            print('Enviando resposta')
            connectionSocket.send(outputdata)
            print('Resposta enviada')

        except IOError:
            #Send response message for file not found
            errorMessage = b'HTTP/1.1 404 Not Found\r\n\r\nArquivo nao encontrado'
            connectionSocket.send(errorMessage)

        #Close client socket
        connectionSocket.close()

    elif message.startswith("POST"):
        try:    
            if "username=pedro&password=jambo" in message:
                print('login correto')

                f2 = open('home.html', 'rb')
                outputdata2 = f2.read()
                print('Arquivo aberto')
                f2.close()

                #Get server IP using DNS
                DNS = gethostname()
                IP  = gethostbyname(DNS)

                outputdata2 = outputdata2.replace(b'{{SERVER_IP}}', IP.encode())
                
                #Send one HTTP header line into socket
                header2 = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: ' + str(len(outputdata2)).encode() + b'\r\n\r\n'
                connectionSocket.send(header2)


                connectionSocket.send(outputdata2)
                print('Arquivo enviado')
                
            else:
                print('login incorreto')

                f3 = open('login2.html', 'rb')
                outputdata3 = f3.read()
                print('Arquivo aberto')
                f3.close()

                #Send one HTTP header line into socket
                header3 = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: ' + str(len(outputdata3)).encode() + b'\r\n\r\n'
                connectionSocket.send(header3)
                connectionSocket.send(outputdata3)
                print('Arquivo enviado')


        except IOError:
            #Send response message for file not found
            errorMessage = b'HTTP/1.1 404 Not Found\r\n\r\nArquivo nao encontrado'
            connectionSocket.send(errorMessage)

        connectionSocket.close()

    #sys.exit()#Terminate the program after sending the corresponding data