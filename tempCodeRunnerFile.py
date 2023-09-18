    elif message.startswith("POST"):
        try:    
            if "usuario=admin&senha=1234" in message:
                f2 = open('home.html', 'rb')
                outputdata2 = f2.read()

                #Send one HTTP header line into socket
                header2 = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: ' + str(len(outputdata2)).encode() + b'\r\n\r\n'
                connectionSocket.send(header2)
            else:
                f3 = open('login2.html', 'rb')
                outputdata3 = f3.read()

                #Send one HTTP header line into socket
                header3 = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: ' + str(len(outputdata3)).encode() + b'\r\n\r\n'
                connectionSocket.send(header3)


        except IOError:
            #Send response message for file not found
            errorMessage = b'HTTP/1.1 404 Not Found\r\n\r\nArquivo nao encontrado'
            connectionSocket.send(errorMessage)