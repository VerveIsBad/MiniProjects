import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCCONECT_MESSAGE = "!DISCONNECT"
SERVER = "10.68.1.103"
# Connect to Gloal server? Change to it's public IP ^
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(msg)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


send("Message! UWU")

"""
Client recive message from Server:

if client.recv(2048).decode(FORMAT):
    # stuff here. I think this is how it works.

"""