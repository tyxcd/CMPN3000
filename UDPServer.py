import socket
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort)) 
serverSocket.settimeout(1)  # Set a timeout of 1 seconds
print("The server is ready to receive")
try: #try block to handle the server exceptions
    while True: #infinite server loop
        try: #try block for client comms
            message, clientAddress = serverSocket.recvfrom(2048) #client message reception
            message = message.decode() #client message decoding
            serverSocket.sendto(message.encode(), clientAddress) #echoing message back to client
        except TimeoutError: #timeout exception
            continue
except KeyboardInterrupt: #keyboard interrupt
    print("\nServer is shutting down.") 
finally: #final block to close socket
    serverSocket.close()
