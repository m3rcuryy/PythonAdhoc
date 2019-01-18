
from bs4 import BeautifulSoup
import requests
url="https://en.wikipedia.org/wiki/Facebook"
r=requests.get(url)
data=r.text
soup=BeautifulSoup(data)
for link in soup.find_all('a'):
	print(link.get('href'))
