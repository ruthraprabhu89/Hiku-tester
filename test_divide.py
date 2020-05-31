import divide
import unittest

class Testdivide(unittest.TestCase):
	
	def test_divide(self):
		result = divide.divide(10,5)
		self.assertEqual(result, 2)

if __name__ == '__main__':
	unittest.main()
