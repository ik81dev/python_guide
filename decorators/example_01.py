#-*-coding:utf-8-*-
import sys
from datetime import datetime
from random import randint
from time import sleep
import logging

logging.basicConfig(level=logging.DEBUG)

def mesure_time_decorator(f):
	def wrapper(*args, **kwargs):
		start = datetime.now()
		result = f(*args, **kwargs)
		duration = datetime.now() - start
		return (str(duration), result)
	return wrapper

	
def logging_decorator(f):
	def wrapper(*args, **kwargs):
		logging.debug("Executing function...%s, %s"%(args, kwargs))
		result = f(*args, **kwargs)
		logging.debug("Finished.")
		return result
	return wrapper
	

@logging_decorator
@mesure_time_decorator
def populate(L, n, debug=False,*args, **kwargs):
	if (not isinstance(L, list)) and (not isinstance(n, int)):
		return None
	for i in range(n):
		sleep(0.01)
		L.append(randint(0, 100))
	return L

@mesure_time_decorator
def sample():
	print "Hello world"

	
if __name__ == "__main__":
	sample()
	print populate([], 10, debug=True, verbose=True, timeout=10)
	sys.exit(0)
