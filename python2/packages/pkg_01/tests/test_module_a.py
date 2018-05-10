print "name:", __name__
print "file:", __file__
print "package:", __package__

if __package__ is not None:
	print "This is package:", __package__
	from .. import module_a
else:
	print "This is not a package. Import through sys.path"
	import sys
	sys.path.append("C:\cases\python_guide\packages\pkg_01")
	import module_a

def test_add_integers():
	"""
		Test funkcji add_integers.
	"""
	a = 10
	b = 20
	result = 30
	print "Testing..."
	if module_a.add_integers(a, b) == result:
		return "SUCCESS"
	else:
		return "FAILURE"
		

#print test_add_integers()
		
if __name__ == "__main__":
	print __name__
	test_add_integers()