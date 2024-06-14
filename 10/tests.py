from coins import exchange
import unittest


class SolutionTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		""" set up for class """
		print("COIN EXCHANGE TESTS")
		print("===================")
		
	@classmethod
	def tearDownClass(cls):
		""" tear down for class """
		print("===================")
		
	def setUp(self):
		""" set up for test """
		print('\n')
		# print('Set up for [' + self.shortDescription() + ']')

	def tearDown(self):
		""" tear down for test """
		# print('Tear down for [' + self.shortDescription() + ']')
		pass
		
	def test_01(self):
		""" 01. [1, 2, 5, 10], 11) == [10, 1] """
		self.assertEqual(exchange([1, 2, 5, 10], 11), [10, 1])
		
	def test_02(self):
		""" 02. ([1, 2, 5], 11) == [5, 5, 1] """				 
		self.assertEqual(exchange([1, 2, 5], 11), [5, 5, 1])
		
	def test_03(self):
		""" 03. ([1, 2, 5, 10], 9) == [5, 2, 2] """
		self.assertEqual(exchange([1, 2, 5, 10], 9), [5, 2, 2])
		
	def test_04(self):
		""" 04. ([2, 5, 10], 1) == [] """
		self.assertEqual(exchange([2, 5, 10], 1), [])
		
	def test_05(self):
		""" 05. ([1, 3, 10], 23) == [10, 10, 3] """
		self.assertEqual(exchange([1, 3, 10], 23), [10, 10, 3])
		
	def test_06(self):
		""" 06. ([1, 5, 10], 28) == [10, 10, 5, 1, 1, 1] """
		self.assertEqual(exchange([1, 5, 10], 28), [10, 10, 5, 1, 1, 1])
		
	def test_07(self):
		""" 07. ([4, 10, 77], 100) == [] """
		self.assertEqual(exchange([4, 10, 77], 100), [])

if __name__ == '__main__':
	unittest.main()

