import solution
import unittest


class SolutionTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		'''Set up for class'''
		print('RADIX SORT SOLUTION TESTS')
		print('==========')
		
		
	@classmethod
	def tearDownClass(cls):
		'''Tear down for class'''
		print('==========')
		
		
	def setUp(self):
		'''Set up for test'''
		print('Set up for [' + self.shortDescription() + ']')
		
		
	def tearDown(self):
		'''Tear down for test'''
		print('Tear down for [' + self.shortDescription() + ']')
		
		
	def prepairing(self, data):
		test_data = []
		solution.data_reading(test_data, data)
	
		sorted_data = sorted(test_data, key=lambda x: x[2])
		expected = solution.data_to_original_format(sorted_data)
	
		solver = solution.PhoneNumbersRadixSort(test_data)
		actual = solver.sort(key=lambda x: x[2])
		
		return (actual, expected)
		
		
	def test_original_data(self):
		'''ORIGINAL DATA TEST'''
		actual, expected = self.prepairing('./data/original_data.txt')
		self.assertEqual(actual, expected)
		
		
	def test_random_order(self):
		'''RANDOM ORDER TEST'''
		actual, expected = self.prepairing('./test_data/test_random_order.txt')
		self.assertEqual(actual, expected)
		
		
	def test_reverse_order(self):
		'''REVERSE ORDER TEST'''
		actual, expected = self.prepairing('./test_data/test_reverse_order.txt')
		self.assertEqual(actual, expected)
		
		
	def test_single_element(self):
		'''SINGLE ELEMENT TEST'''
		actual, expected = self.prepairing('./test_data/test_single_element.txt')
		self.assertEqual(actual, expected)
		
		
	def test_stability(self):
		'''STABILITY TEST'''
		actual, expected = self.prepairing('./test_data/test_stability.txt')
		self.assertEqual(actual, expected)

