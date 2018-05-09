from .. import module

def test_add_integers():
	"""
		Test funkcji add_integers.
	"""
	a = 10
	b = 20
	result = 30
	print "Testing..."
	if module.add_integers(a, b) == result:
		return "SUCCESS"
	else:
		return "FAILURE"
		

#print test_add_integers()
		
if __name__ == "__main__":
	print __name__
	test_add_integers()