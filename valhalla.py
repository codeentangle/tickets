import re
import webbrowser
import urllib
from urllib.request import urlopen
import time

url = 'http://aspx.ebillet.dk/simple/buy.listtt.aspx?act=Buy&refno=42617&orgno=156&sysno=3'
itterations = 0

def queryTickets():
	global itterations
	itterations += 1
	try:
		response = urlopen(url)
		parsed = response.read().decode('utf-8')
		result = re.search("select_tt ticket_type", parsed)

		if result:
			print(str(itterations) + ": Tickets found!!!", end="\r")
			webbrowser.open_new(url)

		else:
			print(str(itterations) + ": No tickets", end="\r")

	except urllib.error.URLError:
		print('Url was not reachable somehow')

while True:
	queryTickets()
	time.sleep(60)
