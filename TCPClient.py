import socket
from socket import *
serverName = '192.168.15.21'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort)) #TCP connection to server
sentence = input('Input sentence:') 
clientSocket.send(sentence.encode())
sentence = clientSocket.recv(1024)
print('From Server:', sentence.decode())
clientSocket.close()
# TCP client program