import socket

HEADER = 64    # defining the header of messages
PORT = 5050    # choosing port, search about why is that specific port
SERVER = socket.gethostbyname(socket.gethostname())    # getting ipv4 by hostname
FORMAT = 'utf-8'    # defining the format of headers
DISCONNECT_MESSAGE = '!DISCONNECT'    # define the disconnect message
ADDR = (SERVER, PORT)    # tuple for binding sockets

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # define client socket
client.connect(ADDR)    # creating the connection with the address

# sending the message
def send(msg):
    message = msg.encode(FORMAT)    # encode the message
    msg_length = len(message)    # getting the length of message
    send_length = str(msg_length).encode(FORMAT)    # casting the length of message to be send
    send_length += b' ' * (HEADER - len(send_length))    # getting the real byte length of message
    client.send(message)

send('Hello World!')

