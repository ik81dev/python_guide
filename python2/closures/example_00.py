#-*-coding:utf-8-*-
"""
	Przykład użycia domknięcia (obiektu wiążącego funkcję ze środowiskiem mającym wpływ na nią w momencie jej definiowania 
"""


def mulfact(a):
	"""Funkcja zewnetrzna"""
	def mul(b):
		"""Funkcja wewnetrzna"""
		print "Wynik mnozenia: %s * %s = %s"%(a, b, a * b)
		return a * b
		
	print "Zwracam funkcje do mnozenia przez: ", a
	return mul
	

print mulfact(2)(3)
