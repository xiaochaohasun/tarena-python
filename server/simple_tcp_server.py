#!/usr/bin/env python

import socket


host=''
port=1234

addr=(host,port)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind(addr)
s.listen(1)
while True:
    cli_sock, cli_addr = s.accept()  # yum install -y telnet
    print "Client connected from:", cli_addr # telnet 127.0.0.1 1234
    while True:
        cli_sock.send("I C U\r\n")
        data=cli_sock.recv(1024)
        if data.strip() == '':
            break
        print data,
    cli_sock.close()

s.close()