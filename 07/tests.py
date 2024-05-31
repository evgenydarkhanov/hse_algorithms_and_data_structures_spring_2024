from typing import Optional

from boyermoore import shift_hashmap, boyer_moore_search

import unittest


class SolutionTestCase(unittest.TestCase):


	@classmethod
	def setUpClass(cls):
		""" set up for class """
		print("BOYER-MOORE TESTS")
		print("=================")
		
	@classmethod
	def tearDownClass(cls):
		""" tear down for class """
		print("=================")
		
	def setUp(self):
		""" set up for test """
		print('\n')
		# print('Set up for [' + self.shortDescription() + ']')

	def tearDown(self):
		""" tear down for test """
		# print('Tear down for [' + self.shortDescription() + ']')
		pass
		
	def test_01(self):
		""" 01. SUBSTRING == STRING """
		text = 'cab'
		pattern = 'cab'
		result = boyer_moore_search(text, pattern)
		self.assertEqual([1], result)
		
	def test_02(self):
		""" 02. SUBSTRING LENGTH > STRING LENGTH """
		text = 'cab'
		pattern = 'caba'
		result = boyer_moore_search(text, pattern)
		self.assertIsNone(result)
		
	def test_03(self):
		""" 03. SUBSTRING AT THE BEGINNING OF THE STRING """
		text = 'acabcbcd'
		pattern = 'cab'
		result = boyer_moore_search(text, pattern)
		self.assertEqual([2], result)
		
	def test_04(self):
		""" 04. SUBSTRING IN THE MIDDLE OF THE STRING """
		text = 'badgabacafkjfkj'
		pattern = 'aba'
		result = boyer_moore_search(text, pattern)
		self.assertEqual([5], result)
		
	def test_05(self):
		""" 05. SUBSTRING AT THE END OF THE STRING """
		text = 'bafytdafybac'
		pattern = 'bac'
		result = boyer_moore_search(text, pattern)
		self.assertEqual([10], result)
		
	def test_06(self):
		""" 06. SUBSTRING IS NOT IN THE STRING """
		text = 'abcdefg'
		pattern = 'h'
		result = boyer_moore_search(text, pattern)
		self.assertIsNone(result)
		
	def test_07(self):
		""" 07. SUBSTRING IS INCLUDED SEVERAL TIMES """
		text = 'aaabaaaaabaaaaabaaaaba'
		pattern = 'abaa'
		result = boyer_moore_search(text, pattern)
		self.assertEqual([3, 9, 15], result)
		
	def test_08(self):
		""" 08. STRING CONSISTS OF SUBSTRINGS """
		text = 'abababababa'
		pattern = 'aba'
		result = boyer_moore_search(text, pattern)
		self.assertEqual([1, 3, 5, 7, 9], result)
		

if __name__ == '__main__':
	unittest.main()

