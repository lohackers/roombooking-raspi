#!/usr/bin/env python

import ConfigParser
import urllib2
from time import sleep
from json import loads
import os

# Set configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Get configuration
upcoming = config.get('DEFAULT', 'upcoming')
onair = config.get('DEFAULT', 'onair')
polling = int(config.get('DEFAULT', 'polling'))

# Main routine
def main():
	opener = urllib2.build_opener()
	opener.addheaders = [('Accept', 'application/json')]

	while True:
		upcoming_booking = len(loads(opener.open(upcoming).read()))
		onair_booking = len(loads(opener.open(onair).read()))

		if onair_booking:
			# There is a live event, turn on RED light
			print 'ON AIR NOW!'
		elif upcoming_booking:
			# There is a booking soon, turn on ORANGE light
			print 'EVENT IS COMING SOON'
		else:
			# No events, turn off ALL lights
			print 'NO EVENTS!'

		sleep(polling)

# Call main
if __name__ == '__main__':
	main()