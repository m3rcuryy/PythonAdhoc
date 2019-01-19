
from bs4 import BeautifulSoup
import requests
url="https://en.wikipedia.org/wiki/Facebook"
r=requests.get(url)
data=r.text
soup=BeautifulSoup(data)
scrap=""
for link in soup.find_all('p'):
	scrap=scrap+link.text
print scrap
