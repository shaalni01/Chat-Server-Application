import socket
import threading

# Connection Data
host = '127.0.0.1'
port = 55555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Sending Messages To All Connected Clients
def broadcast(message):
        #broadcasting
        for client in clients:
            client.send(message)

def direct_message(message,client):
    #sending direct message
    if client in nicknames:
        index = nicknames.index(client)
        print(index)
        client2=clients[index]
        client2.send(message)
        return True
    else:
        return False

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            A=message.split()
            print(A)
            #print(string2)
            if(A[1]=="/dm".encode('ascii')):
                C=A[0].decode()
                for i in range(3,len(A)):
                    C=C+" " \
                        ""+A[i].decode()
                #print(C)
                hehe = direct_message(C.encode('ascii'),A[2].decode())
                
                if not hehe:
                    msg = "The client you are trying to chat with is not in the server"
                    client.send(msg.encode('ascii'))
            #print("ABC",message)
            elif (A[1] == "/bm".encode('ascii')):
                C = A[0].decode()
                for i in range(2, len(A)):
                    C = C + " " + A[i].decode()
                broadcast(C.encode('ascii'))
            elif (A[1]=="/help".encode('ascii')):
                K="dm- direct message, bm- broadcast message "
                L="help- lists commands, users- lists the current users"
                client.send(K.encode('ascii'))
                client.send(L.encode('ascii'))
            elif (A[1] == "/quit".encode('ascii')):
                index = nicknames.index(A[2].decode())
                clients.remove(clients[index])
                client.close()
                nickname = nicknames[index]
                broadcast('{} left!'.format(nickname).encode('ascii'))
                nicknames.remove(nickname)
            elif (A[1] == "/users".encode('ascii')):
                #C = A[0].decode()
                C=""
                if(len(nicknames) == 1):
                    C = C + nicknames[0]
                    client.send(C.encode('ascii'))
                else:
                    for i in range(0, len(nicknames)-1):
                        C = C+ nicknames[i]+","
                    C = C+nicknames[i+1]
                    client.send(C.encode('ascii'))
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()

