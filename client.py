#!usr/bin/env python2

import socket
ip="127.0.0.1"
port=9090
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # AF_INET is for ipv4 and SOCK_DGRAM is for UDP

# sending messahe to target

while True:
	data=raw_input("enter your command:\n")
	# it will send data to receiver as well as create its own socket(own ip and random port)
	s.sendto(data,(ip,port)) # providing a way to connect
	print s.recvfrom(100)[0]	

