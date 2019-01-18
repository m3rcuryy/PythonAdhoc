#!usr/bin/env python2

import socket
ip="127.0.0.1"
port=9090
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # AF_INET is for ipv4 and SOCK_DGRAM is for UDP

# sending messahe to target

s.bind((ip,port)) #providing a way to connect

while True:	
	rec_data=s.recvfrom(100)  #here 100 is buffer size in char
	print "data received from client: " + rec_data[0]
	#s.sendto("ok got it",rec_data[1]) # here rec_data[1] is combo of ip and port of sender
