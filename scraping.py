#!/usr/bin/python 
import  urllib2
from  googlesearch  import  search
from bs4 import BeautifulSoup
import requests
import time
# now put a keyword
srch=raw_input("enter keyword to search:\n")
webdata=search(srch,num=3,tld="co.in")
#webdata=search('hello',num=3,stop=2,pause=1)
#  generator type  iterable 

time.sleep(5)
final_data=[]
for  url  in   webdata:
	print url
	time.sleep(2)
	#url="https://en.wikipedia.org/wiki/Facebook"
	res=requests.get(url)
	html_code=res.text
	soup=BeautifulSoup(html_code,'html.parser')
	data=""
	for temp in soup.find_all('p'):
        	data=data+temp.text
	print data
	time.sleep(2)
	final_data.append(data)


