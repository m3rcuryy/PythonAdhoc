#!usr/bin/env python2

import socket
SOCKETS=[("127.0.0.1",9090),("127.0.0.1",9091)]
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # AF_INET is for ipv4 and SOCK_DGRAM is for UDP

# sending messahe to target

while True:
	data=raw_input("type your message:\n")
# it will send data to receiver as well as create its own socket(own ip and random port)
	for recv in SOCKETS:	
		s.sendto(data,recv)	
	#print "reply: " + s.recvfrom(10)[0]

