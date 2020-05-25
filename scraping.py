import requests
from bs4 import BeautifulSoup

r = requests.get('https://baseballdata.jp/playerB/1200069_3.html')
r.encoding = r.apparent_encoding

soup = BeautifulSoup(r.content, "html.parser")

print(soup.find("title").text)