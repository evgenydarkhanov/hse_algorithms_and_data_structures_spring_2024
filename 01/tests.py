import solution
import unittest


class SolutionTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		'''Set up for class'''
		print('QUICK SORT SOLUTION TESTS')
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
		expected = sorted(test_data, key=lambda x: x[0])
		solution.quick_sort_and_partition(test_data, key=lambda x: x[0])
		return (test_data, expected)
		
		
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
		test_data = []
		actual, expected = self.prepairing('./test_data/test_stability.txt')
		if actual == expected:
			print('stable')
		else:
			print('unstable')
		self.assertIsNot(actual, expected)

