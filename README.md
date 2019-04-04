# Special-Laboratory-in-Computer-Science-and-Engineering-II-CS394-


Your assignment is to build a server capable of receiving text messages from clients. The server should print these text messages on the standard output, but should not print any other messages such as debug information. From the server perspective, a message corresponds to the data received from a particular client during a communication session with that client. The server should be listening for text messages to a port known to the clients. The server should be able to queue connections from multiple clients i.e., it will handle the client connections sequentially, but should be able to accept connections from multiple clients. After servicing the current client to completion, it should proceed to the next. If multiple clients simultaneously try to send text messages to the server, the server should print them one at a time (in any order). Note that you don't have to implement an event-driven or multi-threaded server. Serving one client at a time is enough. 

We also want you to write a client. The client should read from a file, transmit the message and exit.
You can assume that the client is run as "client server-IP-address port-number" where server-IP-address is the IP address of the server, and port-number is the TCP port the server listens on. The server is run as "server port-number". If the server cannot bind on a port, print a message to standard error.
Make sure you handle the following correctly:
1. Buffer management: Assume that the file contents can be arbitrarily large (assume a typical size of 20KB), but the buffers you use to read/write to the file or socket must be small and of fixed size (e.g., 4096 bytes).
2. Handling return values: By default, sockets are blocking, and for this assignment we will use only blocking sockets. "Blocking" means that when we issue a socket call that cannot be done immediately (including not being able to read or write), our process is waits until it can perform the action. This includes the case when
(a) a socket's internal buffer is full and therefore, no data can be written, or
(b) a socket's buffer is empty, and no data is available to be read.
However, if there is some data available to be read or some can be written, the call will return the number of bytes read or written respectively. NOTE: This returned value can be less than specified in the length argument to the call or indicate an error. 

Programming with Python (Multiplexing sockets I/O modules): 
[11]	Write a simple web server that can return a single line/multiple line of text to any connected web browser.

[12]	Write an efficient chart server that can handle several hundred or a large number of client connections. The chart server initializes with a few data attributes. It stores the count of clients, map of each client, and output sockets.  The chart client initializes with a name argument and sends this name to the chart server.
[13]	Write program for local port forwarder, that will redirect all traffic from a local port to a particular remote host?

[14]	Write a client that will wait for a particular network service forever or for a time out?

[15]	Write a program to list the network interfaces present in your machine?

[17] Extend the client/server interaction to simulate a password dialogue. After receiving data from a client, the server returns access granted or access denied depending on whether the received data matches the password.  
[18]  Write a program that compress your working directory and email to a specific address? 
[19] Write a python script to check email message from your Google account with Internet Message Access Protocol) IMAP. 
[20] Write a program to send an email to one or multiple users with an attachment via Gmail with Simple Mail Transfer Protocol (SMTP) server.  
[21] Write a program that establish secure connection to email server as Google or Yahoo through SMTP client secured with Transport layer security (TLS).  

[22]	Write a program to demonstrate the loading of a local file to a remote FTP?
[23]	Write a program that compress your current working directory   and then email as a message.  You can send the email message via an external Gmail SMTP host, or you can use a local email server to do this. 
[24]	Write a program that connects to your Google email account and read the email message. Display one or multiple email message on user request.
[25]	Write a program that finds detail of the mail server from an email address.
 [26]	Write a program that connects to Google mail server with POP3 to fetch an email message from an email account.
[27] Write a program that establish a connection with a remote machine over SSH. Then display the remote machine’s CPU and Main memory information. 
N.B. you need to install third party package Paramiko 
 
[28] Demonstrate the use of executing a MYSQL command on remote server (i.e. you may create MYSQL database for the student,s of BTech 8th semester). 
 
[29] Write a multithreaded, multi call XML-RPC server, so that multiple function calls can return a single result? 
 
[30] In corporate a suitable authentication scheme to the serve designed in question number 29. 
====================================================================================================================
