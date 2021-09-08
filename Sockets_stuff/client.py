import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCCONECT_MESSAGE = "!DISCONNECT"
SERVER = "10.68.1.103"
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

