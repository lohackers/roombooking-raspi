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
api_endpoint = config.get('DEFAULT', 'api_endpoint')
polling = int(config.get('DEFAULT', 'polling'))

# Main routine
def main():
	opener = urllib2.build_opener()
	opener.addheaders = [('Accept', 'application/json')]

	while True:
		bookings = loads(opener.open(api_endpoint).read())
		print bookings[0]['from']

		sleep(polling)

# Call main
if __name__ == '__main__':
	main()