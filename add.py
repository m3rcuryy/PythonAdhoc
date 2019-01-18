#!/usr/bin/python2

import cgi,cgitb # to receive data from web server
cgitb.enable() # to display error in this file
print "Conten-type:text/html"
print ""

web_data=cgi.FieldStorage()

#extracting n1 and n2 or extracting variables from html page

x=web_data.getvalue('n1')
y=web_data.getvalue('n2')
c=web_data.getvalue('cmd')

print int(x)+int(y)

print "<pre>"
	print commands.getoutput('sudo ' + c)
print "<pre>"
x='''
<b>hello</b>
'''
print x
