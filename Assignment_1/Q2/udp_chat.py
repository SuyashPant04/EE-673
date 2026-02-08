from socket import *
import threading

PHONE_IP = "172.23.7.100"
PHONE_PORT = 5005

PC_PORT = 5006

sock = socket(AF_INET, SOCK_DGRAM)  # UDP socket creation
sock.bind(('', PC_PORT))  # Binding the socket to the port

print("The server is ready to receive")  # Server ready message

def receive_message():
    while True:
        message, clientAddress = sock.recvfrom(2048)  # To Receive message from client
        print("\nPhone: ", message.decode())  # Print message received from phone

recv_thread = threading.Thread(target=receive_message)  # Create a thread for receiving messages
recv_thread.start()  # Start the receiving thread

def send_message():
    while True:
        message = input("PC: ")  # Get user input
        sock.sendto(message.encode(), (PHONE_IP, PHONE_PORT))  # Send message to phone

send_thread = threading.Thread(target=send_message)  # Create a thread for sending messages
send_thread.start()  # Start the sending thread
