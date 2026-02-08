from socket import * # Import socket module

serverPort = 12345 # Port to listen on

serverSocket = socket(AF_INET, SOCK_DGRAM) # Create a UDP socket

serverSocket.bind(('', serverPort)) # Bind the socket to the port

print("The server is ready to receive") # Loop to continuously receive messages from clients

while True:
    message, clientAddress = serverSocket.recvfrom(2048) # Receive message from client
    modifiedMessage = message.decode().upper() # Convert message to uppercase
    serverSocket.sendto(modifiedMessage.encode(), clientAddress) # Send modified message back to client