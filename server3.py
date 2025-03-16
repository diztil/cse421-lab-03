import socket # import the necessary library
import threading # import

format = "utf-8" # decoding/encoding format for the message text
buffer_size = 16 # maximum value for receiving
host_name = socket.gethostname() # store the host name after getting it
ip_addr = socket.gethostbyname(host_name) # store the ip address
port = 5050 # define a port number
server_sock_addr = (ip_addr, port) # store server socket address as tuple

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a server
server.bind(server_sock_addr) # set the server socket address using "ip_addr, port"tuple
server.listen() # now the server can listen for clients
print("Server is listening on port: ", str(port)) # just a print statement to know the server is ready

def handle_clients(conn, addr): # function for individually handling clients
    if message == "Bye": # if the client sends message that says "Bye"
        conn.send("Goodbye".encode(format)) # send a message to client
        print("Terminating connection with", addr) # print message to console
        connected = False # disconnect
    else: # otherwise, if it is a normal message
        print(message) # show message on console
        vowels = "aeiouAEIOU" # define a set of all possible English vowels
        count = 0 # keep a track of the number of vowels
        for i in message: # check every char in the message
            if i in vowels: # if the char is a vowel
                count += 1 # increase counter
        conn.send(str(count).encode(format)) # send a message to client containing number of vowels


while True: # continuously keep checking for any client messages
    conn, addr = server.accept() # accept any incoming connections and set the values to a socket (conn) and socket address (addr)
    print("Connect to:",addr) # show which client is connected
    connected = True # set the connected status
    while connected: # as long as the server is connected to client
        msg_len = conn.recv(buffer_size).decode(format) # decode the previously encoded (in client) message
        print("Length of the upcoming message:",msg_len) # show the message size
        if msg_len: # if the message length exists (is received)
            message = conn.recv(int(msg_len)).decode(format) # convert message size to int, after decoding
            
    conn.close() # close the connection, disconnect further

    # ===== NOTES =====
    # the port number may show random numbers every time because of getting random process IDs