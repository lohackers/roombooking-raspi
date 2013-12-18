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

os.system("gpio mode 0 out")
os.system("gpio mode 1 out")

# Main routine
def main():
	opener = urllib2.build_opener()
	opener.addheaders = [('Accept', 'application/json')]

	while True:
		upcoming_booking = len(loads(opener.open(upcoming).read()))
		onair_booking = len(loads(opener.open(onair).read()))

		if onair_booking:
			os.system("gpio write 1 1")
			os.system("gpio write 7 0")
			print 'ON AIR NOW!'
		elif upcoming_booking:
			os.system("gpio write 1 0")
			os.system("gpio write 7 1")
			print 'EVENT IS COMING SOON'
		else:
			os.system("gpio write 1 0")
			os.system("gpio write 7 0")
			print 'NO EVENTS!'

		sleep(polling)

# Call main
if __name__ == '__main__':
	main()