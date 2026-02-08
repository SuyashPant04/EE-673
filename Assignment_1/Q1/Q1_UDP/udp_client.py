from socket import *   # Import socket module

serverName = 'localhost'  # Server address
serverPort = 12345       # Server port

clientSocket = socket(AF_INET, SOCK_DGRAM)  # Create a UDP socket
message = input("Input Lowercase sentence: ")  # Get user input

clientSocket.sendto(message.encode(), (serverName, serverPort))  # Send message to server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)  # Receive modified message

print("From Server: ", modifiedMessage.decode())  # Print Uppercase sentences from server
clientSocket.close()  # Close the socket