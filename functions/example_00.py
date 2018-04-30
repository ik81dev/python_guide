def f0():
	"""Brak argumentow oraz wartosci zwracanej"""
	pass

def f1():
	"""Funkcja nie ma argumentow zwraca int"""
	return 0

def f2(p1):
	"""Funkcja moze przyjac jeden parametr(argument) pozycyjny"""
	return None

def f3(p1, p2, p3):
	"""Funkcja moze przyjac 3 parametr(argument) pozycyjny"""
	return None

def f4(*args):
	"""
		Funkcja moze przyjac dowolna liczne parametrow
		jednak nie moze przyjac argumentow nazwanych typu klucz=wartosci
	"""
	return args
	
def f5(a, b, c, *args):
	"""Funkcja moze przyjac dowolna liczne parametrow"""
	return args
	
def f6(*args, **kwargs):
	"""
		Funkcja moze przyjac
	"""
	return args, kwargs

