#SMTP Server : mmtp.iitk.ac.in
# SMTP Port   : 25
# Protocol    : SMTP over TCP

import socket
import ssl
import base64
import os 

#server details
smtp_server = "mmtp.iitk.ac.in"
smtp_port = 25

#socket creation
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((smtp_server, smtp_port))

# Receive the server's initial response
response = client_socket.recv(1024).decode()
print("Server:", response)
# Expected response: "220 mmtp.iitk.ac.in"    

#send EHLO command
def send_cmd(cmd):
    print("C:", cmd)
    client_socket.sendall((cmd + "\r\n").encode())
    reply = client_socket.recv(4096).decode()
    print("S:", reply)
    return reply

send_cmd("EHLO localhost") 

send_cmd("STARTTLS") # Expected response: "220 Ready to start TLS"

# Wrap the socket with SSL for secure communication
context = ssl.create_default_context()
client_socket = context.wrap_socket(client_socket, server_hostname=smtp_server)

send_cmd("EHLO iitk.ac.in")

#AUTH LOGIN
send_cmd("AUTH LOGIN") 
# Expected response: "334 VXNlcm5hbWU6" i.e. "334 Username:" in base64 format

username = "user_id@iitk.ac.in"
encoded_username = base64.b64encode(username.encode()).decode() #encoding the username in base64 format
send_cmd(encoded_username)
# Expected response: "334 UGFzc3dvcmQ6" i.e. "334 Password:" in base64 format
password = "user_password"
encoded_password = base64.b64encode(password.encode()).decode() #encoding the password in base64 format
send_cmd(encoded_password)

# Defining recipents details
to_recipients = ["recipient_id@iitk.ac.in"] #edit the receiver email address here
## (ii) of question 3: adding cc and bcc recipients in the email header is optional, you can choose to add them or not by uncommenting the respective lines in the code.
cc_recipients = ["cc_id_1@iitk.ac.in","cc_id_2@iitk.ac.in"] #edit the cc email address here
bcc_recipients = ["bcc_id_1@iitk.ac.in","bcc_id_2@iitk.ac.in"] #edit the bcc email address here


#send email
send_cmd(f"MAIL FROM:<{username}>")
for recipient in to_recipients + cc_recipients + bcc_recipients:
    send_cmd(f"RCPT TO:<{recipient}>")

#part(iii) of question 3: sending an attachment along with the email
attachment_path = "attachment.txt"
attachment_name = os.path.basename(attachment_path)

with open(attachment_path, "rb") as f:
    attachment_data = base64.b64encode(f.read()).decode()

boundary = "BOUNDARY12345"

send_cmd("DATA")
message = (
    f"From: {username}\r\n"
    f"To: {', '.join(to_recipients)}\r\n"
    # f"Cc: {', '.join(cc_recipients)}\r\n" ## (ii) of question 3: adding cc recipients in the email header
    "Subject: Test mail from Python SMTP client\r\n" ## (i) of question 3: subject of the email
    "MIME-Version: 1.0\r\n" ## (iii) of question 3: adding MIME version header to indicate that the email contains multiple parts (text and attachment)
    f"Content-Type: multipart/mixed; boundary={boundary}\r\n"
    "\r\n"
    #---Text part of the email---
    f"--{boundary}\r\n"
    "Content-Type: text/plain\r\n"
    "\r\n"
    "Hello,\r\n"
    "This is a test mail sent using a Python SMTP client by me Suyash.\r\n"
    "\r\n"
    #---Attachment part of the email---
    f"--{boundary}\r\n"
    f"Content-Type: application/octet-stream; name={attachment_name}\r\n"
    "Content-Transfer-Encoding: base64\r\n"
    f"Content-Disposition: attachment; filename={attachment_name}\r\n"
    "\r\n"
    f"{attachment_data}\r\n"
    f"--{boundary}--\r\n"
)

client_socket.sendall(message.encode())
send_cmd(".") # End of message
send_cmd("QUIT") # Close the connection
client_socket.close()
