import socket 
import threading


HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
# Want to be non-local? Change to pulic IP adress ^^^
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCCONECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)



def handle_client(conn, addr):

    # Shows client IP
    print(f"[NEW CONNECTION] {addr} connected.")

    # Starts the loop; this happens after the thread starts this function.
    connected = True 
    while connected:
        """
        Message is received in bytes, so we decode this and convert it into the length of the message
        Server: receives bytes message
        Message: '(message length) 7 (Insert spaces for padding)'
        """
        msg_length = conn.recv(HEADER).decode(FORMAT)
        # Does message actually contain text / real message?
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            # Checks if the client has sent the, "Disconnect message"
            if msg == DISCCONECT_MESSAGE:
                connected = False  
        
            print(f"[{addr}] {msg}")
            '''
            Server to client messaging:

            conn.send('MEssage stuHEhehepodv'.encode(FORMAT))
            '''
    
    conn.close()


def start():
    server.listen()
    # Prints the server IP
    print(f"[LISTENING] server is linstening on: {SERVER}")
    
    while True:
        conn, addr = server.accept()
        # directs a thread to the target function, and shows it's arguemnts.
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

# Starts server
print("[SERVER IS STARTING . . .]")
start()

