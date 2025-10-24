import socket
from socket import *
serverPort = 12000 
serverIP = '' 
serverSocket = socket(AF_INET, SOCK_STREAM) #tcp welcome socket creation
serverSocket.bind((serverIP, serverPort)) #bind to address and port
serverSocket.listen(1) #server listens for tcp requests
print('The server is ready to receive')
while True: #infinite loop for server
    connectionSocket, addr = serverSocket.accept() #server waits for incoming requests
    print('Connection from:', addr) #display client address when request is received
    try: #try block to handle client communication
        sentence = connectionSocket.recv(1024).decode() #read bytes from socket
        if not sentence: #check for empty message
            print('Client disconnected.') 
        else:#
            connectionSocket.send(sentence.encode())
    except (ConnectionResetError, BrokenPipeError) as e: #handle connection errors, broken pipe is for sending on closed connection
        print(f"An error occurred with {addr}: {e}") #detailed error message
    finally:
        connectionSocket.close() #close connection socket
        print(f"Connection with {addr} closed.")


