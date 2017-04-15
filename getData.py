from urllib.request import urlopen
from bs4 import BeautifulSoup

def getData(begin, end):
	url = "http://192.168.1.11/values"
	html = urlopen(url).read()
	soup = BeautifulSoup(html, "html5lib")

	for script in soup(["script", "style"]):
		script.extract()

	text = soup.body.get_text()
	return float(text[begin:end])

pm25 = getData(94,98)
pm10 = getData(116,120)
temp = getData(143,148)
hum = getData(174,179)

print(pm25)

