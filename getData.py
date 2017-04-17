from urllib.request import urlopen
from bs4 import BeautifulSoup
import mysql.connector as mysql
import time
import getpass

dbuser = input("MySQL username: ")
dbpass = getpass.getpass("MySQL password: ")
db = mysql.connect(host = "localhost", user = dbuser, passwd = dbpass, db = 
"PARTICLEDATA", buffered = True, autocommit = True)
cur=db.cursor()

def getData(begin, end):
	url = "http://192.168.1.11/values"
	html = urlopen(url).read()
	soup = BeautifulSoup(html, "html5lib")

	for script in soup(["script", "style"]):
		script.extract()

	text = soup.body.get_text()
	return float(text[begin:end])

def getDate():
	return time.strftime("%Y") + "-" + time.strftime("%m") + "-" 
	+ time.strftime("%d")
def getTime():
	return time.strftime("%H") + ":" + time.strftime("%M") + ":00"
def saveToDatabase(pm25, pm10, temp, hum, currentDate, currentTime):
	pm25 = str(pm25)
	pm10 = str(pm10)
	temp = str(temp)
	hum = str(hum)
	mysql = "INSERT INTO MAIN VALUES('" + pm10 + "','" + pm25 + "','" + temp + "','" + hum + "','" + currentDate + "','" + currentTime + "')"
	cur.execute(mysql)
	return

pm25 = getData(94,98)
pm10 = getData(117,121)
temp = getData(144,149)
hum = getData(174,179)
currentDate = getDate()
currentTime = getTime()

saveToDatabase(pm25, pm10, temp, hum, currentDate, currentTime)
print(pm25)
time.sleep(1600)
