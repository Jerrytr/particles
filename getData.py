from urllib.request import urlopen
from bs4 import BeautifulSoup
import mysql.connector as mysql
import time
import getpass

dbuser = input("MySQL username: ")
dbpass = getpass.getpass("MySQL password: ")
db = mysql.connect(host = "localhost", user = dbuser, passwd = dbpass, db = 
"PARTICLES", buffered = True, autocommit = True)

def getData(begin, end):
	url = "http://192.168.1.11/values"
	html = urlopen(url).read()
	soup = BeautifulSoup(html, "html5lib")

	for script in soup(["script", "style"]):
		script.extract()

	text = soup.body.get_text()
	return float(text[begin:end])

pm25 = getData(94,98)
pm10 = getData(117,121)
temp = getData(143,148)
hum = getData(174,179)

print(pm25)

