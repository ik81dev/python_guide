#-*-coding:utf-8-*-

"""
	Przykład użycia domknięcia (obiektu wiążącego funkcję ze środowiskiem mającym wpływ na nią w momencie jej definiowania 
"""

import math


def mulfact_ex(a):
	"""Funkcja zewnetrzna"""
	def mul_a(b):
		"""Funkcja wewnetrzna"""
		def mul_b(c):
			print "Zwracam wynik mnozenia {!r}".format(*[a, b, c])
			return a * b * c
		print "Zwracam funkcję %s"%mul_b
		return mul_b
		
	print "Zwracam funkcje do mnozenia przez: ", a
	return mul_a
	
	
assert mulfact_ex(1)(2)(3) == math.factorial(3), "Cos poszlo nie tak"
	




