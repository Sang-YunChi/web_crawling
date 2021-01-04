from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://news.daum.net/")

bsObject = BeautifulSoup(html, "html.parser") #처음 셀렉터 지정

for link in bsObject.find_all('img'):
    print(link.text.strip(), link.get('src'))
