#!/usr/bin/env python

import ConfigParser

# Set configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

def main():
	print config.get('DEFAULT', 'api_endpoint')

if __name__ == '__main__':
	main()