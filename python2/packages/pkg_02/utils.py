__VERSION__ = "1.0.0"

import networking
import networking.http
from networking.http import get
from networking import http
from .config import CONFIG

def f():
	print "Funkcja narzedziowa"

	
def toupper(msg):
	return msg.upper()
	
def do_get_request():
	#networking.http.get()
	#get()
	http.get()