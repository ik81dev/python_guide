#-*-coding:utf-8-*-
import os
import sys
import logging
import unittest
import argparse

"""
	Description: 
		
	Author: 
	Wersion:
	Date:
"""

module_logger = logging.getLogger(__name__)
module_logger.debug("Module mame %s", __name__)

class Program(object):
	"""Sample """
	def __init__(self, logger=None):
		self.logger = logger or logging.getLogger(Program.__name__)
		self.logger.debug("Konstruktor...")
	
	def run(self):
		self.logger.debug("run")
		
		
if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)
	module_logger.debug("Module logger...")
	parser = argparse.ArgumentParser(description='Description')
	"""Positional args"""
	#parser.add_argument('integers', metavar='int', nargs='+', type=int, help='an integer to be summed')
	parser.add_argument("command", help="Polecenie")
	"""Optional args"""
	#parser.add_argument('--log', default=sys.stdout, type=argparse.FileType('w'), help='the file where the sum should be written')
	
	args = parser.parse_args()
	if args.command == "run":
		Program().run()
	
	