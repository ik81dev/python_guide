import unittest
from .. quizz import QuizzItem

class TestLoad(unittest.TestCase):
	"""
		Test 
	"""
	
	def test_loadfromstring1(self):
		qi = QuizzItem()
		self.assertEqual(1,1)
	
	def test_loadfromstring2(self):
		self.assertEqual(1,1)
	
	def test_loadfromstring3(self):
		self.assertEqual(1,1)
	

	
if __name__ == "__main__":
	unittest.main()

	
	