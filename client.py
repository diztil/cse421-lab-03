import socket # import the necessary library

format = "utf-8" # encoding format for the message text
buffer_size = 16 # setting a value for the maximum size that can be sent
host_name = socket.gethostname() # store the server's host name after getting it
ip_addr = socket.gethostbyname(host_name) # store the server's ip address
port = 5050 # define server's port number
server_sock_addr = (ip_addr,port) # store as a tuple

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a client
client.connect(server_sock_addr) # connect to the server

def msg_to_be_sent(message): # function for easily sending messages
    send_message = message.encode(format) # encoding the message first, e.g. "hello"
    length = len(send_message) # setting the message length by the message text length, e.g. 5
    sending_length = str(length).encode(format) # size of message, e.g. "5"; len of 5 = 1
    # here, we are making sure every message size is the same size, e.g. 16 (buffer_size);
    # suppose a message is less than 16 bytes, then what happens?  Simple: we fill in empty spaces to FORCE it to become 16-bytes long!
    sending_length += b" " * (buffer_size - len(sending_length)) # fill in any empty spaces at the end, e.g. "5          "
    client.send(sending_length) # first send the SIZE of the message to the server
    client.send(send_message) # then send the actual message to the server
    # also have the ability to receive any messages from the server
    received_msg = client.recv(2048).decode(format) # set a port 2048 for client listening
    print(received_msg) # show it on console

msg_to_be_sent(f"Hello, the client's ip address is {ip_addr} and the hostname is {host_name}.") # send a sample message to the server
msg_to_be_sent("Bye") # send another message