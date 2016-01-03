#!/usr/bin/env python
# encoding: utf-8

import socket
target_host = 'www.caimaoy.com'
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
client.send("GET / HTTP/1.1\r\nHost: caimaoy.com\r\n\r\n")
recv_len = 1
response = ''
while recv_len:
    data = client.recv(4096)
    recv_len = len(data)
    response += data
    if recv_len < 4096:
        print '[*] len = %s' % recv_len
        print repr(data)
    if response.endswith('</html>'):
        break
print response
