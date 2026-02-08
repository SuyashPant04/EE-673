from socket import * # Import socket module

serverPort = 12000 # Port to listen on

serverSocket = socket(AF_INET, SOCK_STREAM) # Create a TCP socket

serverSocket.bind(('', serverPort)) # Bind the socket to the port

serverSocket.listen(1) # Allow one connection at a time

print("The server is ready to receive") # Listen for incoming connections

while True:
    connectionSocket, addr = serverSocket.accept() # Accept a connection from a client
    message = connectionSocket.recv(2048) # Receive message from client
    modifiedMessage = message.decode().upper() # Convert message to uppercase
    connectionSocket.send(modifiedMessage.encode()) # Send modified message back to client
    connectionSocket.close() # Close the connection

