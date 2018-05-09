#	Wersje modulu:
#		1.0.0 
#				- Implementacja funkcji dodajacej dwie liczby.
#		1.0.1
#				- Implementacja mechanizmu sprawdzania typu argumentow przekazywanych do funkci `add_integers`.
#

def add_integers(a, b):
	"""Funkcja dodaje a do b i zwraca wynik"""
	if isinstance(a, int) and isinstance(b, int):
		return a + b
	else:
		raise TypeError("Argumenty funkcji musza byc typu int!")