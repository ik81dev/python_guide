#-*-coding:utf-8-*-
#	Wersje modulu:
#		1.0.0 
#				- Implementacja funkcji dodajacej dwie liczby.
#		1.0.1
#				- Implementacja mechanizmu sprawdzania typu argumentow przekazywanych do funkci `add_integers`.
#

import sys #dla sys.argv


def add_integers(a, b):
	"""Funkcja dodaje a do b i zwraca wynik"""
	print "Inside function, __name__ is:", __name__, " package is:", __package__
	print "Args are: ", sys.argv
	
	if isinstance(a, int) and isinstance(b, int):
		return a + b
	else:
		raise TypeError("Argumenty funkcji musza byc typu int!")
		
		
		
if __name__ == "__main__":
	print "Name:", __name__
	if len(sys.argv) >= 3:
		print "Wynik operacji %s + %s = %s"%(int(sys.argv[1]), int(sys.argv[2]), add_integers(int(sys.argv[1]), int(sys.argv[2])))
	else:
		print "Podaj dwie liczby jako parametry wywołania skryptu."