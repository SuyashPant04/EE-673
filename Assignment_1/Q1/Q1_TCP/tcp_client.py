from socket import *

serverName = 'localhost'  # Server address
serverPort = 12000       # Server port

clientSocket = socket(AF_INET, SOCK_STREAM)  # Create a TCP socket
clientSocket.connect((serverName, serverPort))  # Connect to the server

messege = input("Input Lowercase sentence: ")  # Get user input

clientSocket.send(messege.encode())  # Send message to server

modifiedMessage = clientSocket.recv(2048)  # Receive modified message

print("From Server: ", modifiedMessage.decode())  # Print Uppercase sentences from server
clientSocket.close()  # Close the socket