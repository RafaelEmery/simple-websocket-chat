import socket

HEADER = 64    # defining the header of messages
PORT = 5555    # choosing port, search about why is that specific port
SERVER = socket.gethostbyname(socket.gethostname())    # getting ipv4 by hostname
FORMAT = 'utf-8'    # defining the format of headers
DISCONNECT_MESSAGE = '!DISCONNECT'    # define the disconnect message
ADDR = (SERVER, PORT)    # tuple for binding sockets

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # define client socket
client.connect(ADDR)    # creating the connection with the address

# sending the message
# the text was encoded here and decoded at the server-side and shown on console
def send(msg):
    message = msg.encode(FORMAT)    # encode the message
    msg_length = len(message)    # getting the length of message
    send_length = str(msg_length).encode(FORMAT)    # casting the length of message to be send
    send_length += b' ' * (HEADER - len(send_length))    # getting the real byte length of message
    client.send(send_length)    # sending the length of message
    client.send(message)    # sending the message
    print(client.recv(2048).decode(FORMAT))    # printing the received message

# sending messages
send("Olá mundo? Tudo certo com vocês?")
input()
send("Aqui é o cliente! Estou enviando esta mensagem para você ver que eu estou online :D")
input()
send("Quando eu envio a mensagem, recebo uma confirmação direto do servidor também!")
input()
send("Agora eu vou sair... Até a próxima!")

# disconnecting
send(DISCONNECT_MESSAGE)

