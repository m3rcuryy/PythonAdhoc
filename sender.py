#!usr/bin/env python2

import socket
ip="192.168.10.101"
port=9090
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # AF_INET is for ipv4 and SOCK_DGRAM is for UDP

# sending messahe to target

while True:
	data=raw_input("type your message:\n ")
	s.sendto(data,(ip,port)) # providing a way to connect

