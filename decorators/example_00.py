#-*-coding:utf-8-*-

def decorator(f):
	def wrapper(*args, **kwargs):
		print "Hello from decorator"
		return f(*args, **kwargs)
	return wrapper

	
def sample01():
	"""Przykładowa funkcja bez parametrów"""
	print "Hello world"

print "-Etap 0------------------------------------------"
sample01()
print "Nazwa funkcji: ", sample01.__name__
print "Dokumentacja funkcji: ", sample01.__doc__

print "-Etap 1------------------------------------------"
decorated_sample01 = decorator(sample01)
decorated_sample01()
print "Nazwa funckji: ", decorated_sample01.__name__
print "Dokumentacja funckji: ", decorated_sample01.__doc__

@decorator
def sample02():
	"""Przykładowa funkcja bez parametrów"""
	print "Hello world"

print "-Etap 2------------------------------------------"
print "Nazwa funkcji: ", sample02.__name__
print "Dokumentacja funkcji: ", sample02.__doc__


from functools import wraps

def enhanced_decorator(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		print "Hello from decorator"
		return f(*args, **kwargs)
	return wrapper

@enhanced_decorator
def sample03():
	"""Przykładowa funkcja bez parametrów"""
	print "Hello world"


print "-Etap 3------------------------------------------"
print "Nazwa funkcji: ", sample03.__name__
print "Dokumentacja funkcji: ", sample03.__doc__
