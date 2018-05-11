def mulfact(a):
	"""Funkcja zewnetrzna"""
	def mul(b):
		"""Funkcja wewnetrzna"""
		print "Wynik mnozenia: %s * %s = %s"%(a, b, a * b)
		return a * b
		
	print "Zwracam funkcje do mnozenia przez: ", a
	return mul
	

def mulfact_ex(a):
	"""Funkcja zewnetrzna"""
	def mul_a(b):
		"""Funkcja wewnetrzna"""
		def mul_b(c):
			return a * b * c
		return mul_b
		
	print "Zwracam funkcje do mnozenia przez: ", a
	return mul_a
	
	
	
f5 = mulfact(5)
print type(f5)
print f5(1)
print f5(2)
print f5(3)
print mulfact(2)(20)
print mulfact_ex(2)(3)(5)


f2 = mulfact_ex(2)
f3 = f2(4)
print f3(10)



