#!usr/bin/env python2

import socket
import thread
ip="127.0.0.1"
port=9090
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # AF_INET is for ipv4 and SOCK_DGRAM is for UDP
# sending messahe to target
s.bind((ip,port)) #providing a way to connect
def sending():
	while True:
		data=raw_input("")
	# it will send data to receiver as well as create its own socket(own ip and random port)
		s.sendto("Vinay: "+data,(ip,9091)) # providing a way to connect	
def receiving():
	while True:
		print  s.recvfrom(100)[0]
try:
	thread.start_new_thread(sending,())
	thread.start_new_thread(receiving,())
except:
	print "error"
while True:
	pass
