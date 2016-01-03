#!/usr/bin/env python
# encoding: utf-8

import socket
target_host = 'www.caimaoy.com'
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
client.send("GET / HTTP/1.1\r\nHost: caimaoy.com\r\n\r\n")
while True:
    response = client.recv(4096)
    if not response:
        client.sent('ACK!')
        client.close()
        break
    print response
