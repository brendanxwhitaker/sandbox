#!/usr/bin/env python

import socket


TCP_IP = "76.16.39.133"
TCP_PORT = 22
BUFFER_SIZE = 1024
MESSAGE = b"Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)
