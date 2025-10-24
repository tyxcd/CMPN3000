import socket
from socket import *
serverName = '192.168.15.21' #ip of server
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(10)  #10 second timeout if no response
message = input('Input sentence: ')
try: #try block for client comm + exceptions
    clientSocket.sendto(message.encode(), (serverName, serverPort)) #send message to server
    message, serverAddress = clientSocket.recvfrom(2048) #receive message from server, including buffer size
    print(message.decode()) #print message
except timeout: #timeout
    print("Request has timed out. No response from server.")
finally: #final block to close socket
    clientSocket.close()