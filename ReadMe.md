<h1 align = "center">
CHAT SERVER APPLICATION
</h1>

# Introduction
The created chat client-server application contains two python files: one for the server and the other for the client. The server python file is run in a command prompt, this results in a connection open in the host address of 127.0.0.1 in the port 55555. Multiple client files are run in unique command prompts according to the number of clients that are to be connected to the server using the TCP socket connection and joining the chat server. The basic functionality of the chat server is to create a network of users by connecting them all to the site hosted by the server and all the intra communications within the network are maintained and passed between the clients by the server using the TCP protocol. A total of five commands or actions can be performed by the clients that are connected to the server. These basic functionalities that can be performed by the client are help, broadcast, direct message, and quit.

# Implementation
The host and port address are determined, and a server is started on this port that starts listening for the clients. Every client is assigned an alias name and separate threads for listening and writing are initialized with a unique identification whenever a new client is started. In this way, each client’s individuality is maintained and this helps us in achieving the task of sending personal messages between two clients through the server. For each command, the handler functions are maintained in the server python script that takes the command sent by the client as input. By decoding this input, the server gets to know what type of message or action the respective client wants to perform and the respective calls for the handler functions are made accordingly. In this way, using multithreading, a separate thread is maintained for each client, and using this identity of the thread the intra communication among the clients in the network of the chat server application is maintained successfully.

# WorkFlow Diagram
<img src = "https://github.com/shaalni01/Chat-Server-Application/blob/main/assets/Workflow%20Diagram.png" />

# Execution of the commands
`/users` : This command can be used to get the list of all the clients that are connected to the chat server application.
The sample command that can be used in the command prompt where the client is initiated:
/users

The sample screenshot for the above command:

<img src = "https://github.com/shaalni01/Chat-Server-Application/blob/main/assets/Users%20Command%20Execution.png" />

**Note: The command sends the list of users only to the client that has requested for the users.**

`/dm`: dm stands for direct message. This command can be used to send a direct message to one of the clients that are connected to the chat server application.

The structure of the command is:
/dm [client that receives the message] [the message that must be sent]

The sample command that can be used in the command prompt where the client is initiated:
/dm user2 “hello from the user1 to user2”

The sample screenshot for the above command is:

<img src= "https://github.com/shaalni01/Chat-Server-Application/blob/main/assets/Direct%20Message%20Execution.JPG"
/>

/bm: bm stands for the broadcast message. This command can be used to send a message to all the clients that are connected to the chat server application.

The structure of the command is:
/bm [the message that must be sent]

The sample command that can be used in the command prompt where the client is initiated:
/bm “hello from the user1 to user2”

The sample screenshot for the above command is:

<img src="https://github.com/shaalni01/Chat-Server-Application/blob/main/assets/Broadcast%20Message%20Execution.JPG" />






