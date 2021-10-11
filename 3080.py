import re
import webbrowser
import urllib
from urllib.request import urlopen, Request
import time

url = 'https://www.proshop.dk/Grafikkort/ASUS-GeForce-RTX-3080-TUF-V2-LHR-10GB-GDDR6X-RAM-Grafikkort/2958611'
itterations = 0

def queryTickets():
	global itterations
	itterations += 1
	try:
		response = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}))
		parsed = response.read().decode('utf-8')
		result = re.search("site-btn-addToBasket-lg", parsed)

		if result:
			print(str(itterations) + ": GPU found!!!", end="\r")
			webbrowser.open_new(url)

		else:
			print(str(itterations) + ": No GPU", end="\r")

	except urllib.error.URLError:
		print('Url was not reachable somehow')

while True:
	queryTickets()
	time.sleep(60)
