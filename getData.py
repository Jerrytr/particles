from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://192.168.1.11/values"
html = urlopen(url).read()
soup = BeautifulSoup(html, "html5lib")

for script in soup(["script", "style"]):
	script.extract()

text = soup.body.get_text()
pm25 = float(text[94:98])
pm10 = float(text[116:120])
temp = float(text[143:148])
hum = float(text[174:179])
print(pm25)
print(pm10)
print(temp)
print(hum)
