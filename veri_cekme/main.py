import requests
from bs4 import BeautifulSoup

#Girdiğimiz url'deki content'i getirir
r = requests.get("https://en.yellowpages.com.tr/search?q=cafe&city=Ankara")
#Alınan Html kodları çağırma
# r.content

soup = BeautifulSoup()
soup.find_all("a")