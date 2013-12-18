#!/usr/bin/env python

from charlcd import Adafruit_CharLCD
import ConfigParser
import urllib2
from time import sleep
from json import loads
import os

lcd = Adafruit_CharLCD()

# Set configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Get configuration
upcoming = config.get('DEFAULT', 'upcoming')
onair = config.get('DEFAULT', 'onair')
polling = int(config.get('DEFAULT', 'polling'))

os.system("gpio mode 1 out")
os.system("gpio mode 7 out")

# Main routine
def main():
	opener = urllib2.build_opener()
	opener.addheaders = [('Accept', 'application/json')]

	while True:
		upcoming_booking = loads(opener.open(upcoming).read())
		onair_booking = loads(opener.open(onair).read())
		lcd.clear()

		if onair_booking:
			os.system("gpio write 1 1")
			os.system("gpio write 7 0")

			time_from = onair_booking[0]["from"].split(" ")[1].split(":")
			time_to = onair_booking[0]["to"].split(" ")[1].split(":")

			lcd.message(time_from[0]+":"+time_from[1] + " - " + time_to[0]+":"+time_to[1] + "\n" + onair_booking[0]["user"]["email"].split("@")[0])

		elif upcoming_booking:
			os.system("gpio write 1 0")
			os.system("gpio write 7 1")

			time_from = upcoming_booking[0]["from"].split(" ")[1].split(":")
			time_to = upcoming_booking[0]["to"].split(" ")[1].split(":")

			lcd.message(time_from[0]+":"+time_from[1] + " - " + time_to[0]+":"+time_to[1] + "\n" + upcoming_booking[0]["user"]["email"].split("@")[0])
		
		else:
			os.system("gpio write 1 0")
			os.system("gpio write 7 0")
			lcd.message("NO EVENTS!")

		sleep(polling)

# Call main
if __name__ == '__main__':
	main()
