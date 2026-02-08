# EE673 – Assignment 1

## Overview

This submission contains solutions for Assignment 1 of the course EE673.  
All programs are implemented in Python and tested on a Windows system using the terminal.

The assignment consists of three problems:

- Problem 1: Basics of Socket Programming  
- Problem 2: UDP Chat Application  
- Problem 3: Mail Client  

Each problem has its own folder containing the corresponding Python scripts.

## Folder Structure

```text
assignment_1/
│
├── Q1/
│ ├── Q1_TCP/
│ │ ├── tcp_client.py
│ │ └── tcp_server.py
│ │
│ └── Q1_UDP/
│ ├── udp_client.py
│ └── udp_server.py
│
├── Q2/
│ └── udp_chat.py
│
├── Q3/
│ ├── smtp_mail_client.py
│ └── attachment.txt
│
└── README.md
```


## Problem 1 – Basics of Socket Programming

### Objective

The objective of Problem 1 is to implement basic client–server applications using socket programming in Python to understand the working of UDP and TCP transport protocols.

The problem is divided into two parts:

- Part A: TCP-based client–server communication  
- Part B: UDP-based client–server communication  

In both cases, the client sends a lowercase sentence to the server, the server converts it to uppercase, and sends it back to the client.

### Instructions to Run

#### Part A: TCP Socket Programming

Open a terminal and navigate to the TCP folder:

```bash
cd Q1/Q1_TCP

```

Start the TCP server first:

```bash
python tcp_server.py

```

The server will display:

```text
The server is ready to receive

```

Open a new terminal window and run the TCP client:

```bash
python tcp_client.py

```

Enter a lowercase sentence when prompted:

```text
Input Lowercase sentence:

```

The client will display the uppercase version received from the server:

```text
From Server: <UPPERCASE MESSAGE>
```


The client terminates after receiving the response, while the server continues to listen for new connections.

#### Part B: UDP Socket Programming

Open a terminal and navigate to the UDP folder:

```bash
cd Q1/Q1_UDP
```


Start the UDP server:

```bash
python udp_server.py
```


The server will display:

```text
The server is ready to receive
```


Open a new terminal window and run the UDP client:

```bash
python udp_client.py
```


Enter a lowercase sentence when prompted:

```text
Input Lowercase sentence:
```


The client will display the uppercase message received from the server:

```text
From Server: <UPPERCASE MESSAGE>
```


The server remains active and can serve multiple client requests sequentially.

## Problem 2 – UDP Chat Application

### Objective

The objective of Problem 2 is to implement a UDP-based chat application that enables real-time message exchange between a PC and a mobile phone using socket programming in Python.

The communication is carried out using the UDP transport protocol, where:

- The PC acts as a UDP server and client simultaneously  
- The mobile phone sends and receives messages using a UDP monitoring/chat application  

### How the Program Works

- A UDP socket is created and bound to a fixed port on the PC  
- The program uses multithreading to allow:  
  - One thread for receiving messages from the phone  
  - One thread for sending messages from the PC to the phone  
- Messages typed on the PC terminal are sent to the phone using UDP  
- Messages sent from the phone are received and displayed on the PC terminal  
- Communication continues until the program is manually terminated  

### Instructions to Run

#### Part A: PC Setup (Python Program)

Navigate to the Q2 directory:

```bash
cd Q2

```

Open the file `udp_chat.py` in a text editor or IDE.

Update the mobile phone IP address:

```python
PHONE_IP = "172.23.7.100"
```


Replace this with the actual IP address of the mobile phone.

Ensure the PC and phone are connected to the same Wi-Fi network.

Verify port numbers:

```python
PHONE_PORT = 5005
PC_PORT = 5006
```


These ports must match the configuration in the mobile application.

Run the Python program:

```bash
python udp_chat.py

```

The following message should appear:

```text
The server is ready to receive
```


#### Part B: Mobile Application Setup

Install "UDP Monitor" chat application on the mobile phone.

Configure the mobile application as follows:

- Destination IP: IP address of the PC  
- Destination Port: 5006 (PC_PORT)  
- Source Port: 5005 (PHONE_PORT)  
- Protocol: UDP  

Ensure:

- Mobile phone and PC are on the same network  
- Firewall is disabled or allows UDP traffic on the selected ports  

#### Part C: Communication

Start typing messages on the PC terminal:

```text
PC: hello
```


Messages sent from the PC will appear on the mobile phone.

Messages sent from the mobile phone will appear on the PC terminal as:

```text
Phone: <message>
```


The chat continues in real time until the program is terminated.

## Problem 3 – Mail Client

### Objective

The objective of Problem 3 is to implement a simple SMTP mail client using raw sockets in Python that is capable of:

- Connecting to the IITK SMTP server  
- Securing the connection using STARTTLS  
- Authenticating using AUTH LOGIN  
- Sending an email with:  
  - Subject  
  - Multiple recipients (To / CC / BCC)  
  - File attachment using MIME multipart  

### How the Program Works

- Establishes a TCP connection with the SMTP server  
- Sends EHLO to discover server capabilities  
- Upgrades the connection using STARTTLS  
- Re-issues EHLO after TLS negotiation  
- Authenticates using AUTH LOGIN (Base64-encoded credentials)  
- Sends email using:  
  - MAIL FROM  
  - RCPT TO (for To / CC / BCC recipients)  
  - DATA  
- Constructs a multipart MIME message containing:  
  - Plain text body  
  - Base64-encoded attachment  
- Terminates the SMTP session using QUIT  

### Instructions to Run

Open the file `smtp_mail_client.py` in a text editor or IDE.

Enter your IITK email credentials.

Replace the following variables with valid credentials:

```python
username = "user_id@iitk.ac.in"
password = "user_password"
```


Specify the sender and recipient details.

Update the sender automatically using the same username.

Modify the recipient lists as required:

```python
to_recipients = ["recipient_id@iitk.ac.in"]
cc_recipients = ["cc_id_1@iitk.ac.in", "cc_id_2@iitk.ac.in"]
bcc_recipients = ["bcc_id_1@iitk.ac.in", "bcc_id_2@iitk.ac.in"]
```


CC and BCC recipients are optional and can be modified as needed.

Add or replace the attachment.

Place any text file you want to send in the Q3 directory.

Update the attachment filename if required:

```python
attachment_path = "attachment.txt"
```


Run the SMTP client from the terminal:

```bash
python smtp_mail_client.py
```


Check the recipient’s inbox to verify:

- Subject is visible  
- Correct handling of To / CC / BCC recipients  
- Attachment is received successfully  