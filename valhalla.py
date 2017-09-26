import re
import webbrowser
import urllib
from urllib.request import urlopen
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
import time

url = 'http://aspx.ebillet.dk/simple/buy.listtt.aspx?act=Buy&refno=42617&orgno=156&sysno=3'
debug_url = 'http://192.168.0.12:8080'
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
			Notify.init("Tickets Available")
			Notice = Notify.Notification.new("Tickets Available", url)
			Notice.show()
			webbrowser.open_new(url)

		else:
			print(str(itterations) + ": No tickets", end="\r")

	except urllib.error.URLError:
		print('Url was not reachable somehow')

while True:
	queryTickets()
	time.sleep(60)