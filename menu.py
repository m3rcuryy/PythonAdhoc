#!/usr/bin/env python2
import webbrowser
options='''
Press 1 to check your OS version :
Press 2 to login your facebook account : 
Press 3 to check RAM and CPU in your current machine :
Press 4 to search something in google :
Press 5 to list out all ip and mac in your network : 
'''
print options
# to take input from users in python2
choice=raw_input("enter your choice:\n")

if choice == "1":
	print "MY OS is RHEL "
elif choice=="4":
	data=raw_input("type something to search on google\n")
	webbrowser.open_new_tab('https://www.google.com/search?q='+data)
else:
	print "invalid option"


