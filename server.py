import socket    # importing sockets
import threading    # create multiple threads

HEADER = 64    # defining the header of messages
PORT = 5555    # choosing port, search about why is that specific port
SERVER = socket.gethostbyname(socket.gethostname())    # getting ipv4 by hostname
ADDR = (SERVER, PORT)    # tuple for binding sockets
FORMAT = 'utf-8'    # defining the format of headers
DISCONNECT_MESSAGE = '!DISCONNECT'    # define the disconnect message

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # (data) Tells the socket what type of sockets will connect and (method) streaming data throught the socket
server.bind(ADDR)    # binding the socket to local address

# start a new thread and handle the individual connection
# connection and address as params
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)    # receiving the size of message

        # verify if msg_lenth is valid
        if msg_length:
            msg_length = int(msg_length)    # cast length
            msg = conn.recv(msg_length).decode(FORMAT)    # receiving the message

            # verify if msg is the disconnect message and break while statement
            if (msg == DISCONNECT_MESSAGE):
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Message received".encode(FORMAT))    # sending the message to client

    conn.close()    # closing connection

# start the server and handle and distribute new connections
def start():
    server.listen()    # start listening the server
    print(f"[LISTENING] server is listening on {SERVER}")

    while True:
        conn, addr = server.accept()    # store the address and the object of connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))    # creating a new thread using handle_client function
        thread.start()    # starting the thread

        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}.")    # printing the amount of thread and -1 is because start is always the inicial thread

print("[STARTING] server is starting...")

start()