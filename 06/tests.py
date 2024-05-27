from typing import Optional, Tuple

from trie import TrieNode, Trie

import unittest
	

class SolutionTestCase(unittest.TestCase):

	TEST_TRIE = Trie()

	@classmethod
	def setUpClass(cls):
		""" set up for class """
		print("TRIE TESTS")
		print("==========")
		
	@classmethod
	def tearDownClass(cls):
		""" tear down for class """
		print("==========")
		
	def setUp(self):
		""" set up for test """
		print('\n')
		# print('Set up for [' + self.shortDescription() + ']')

	def tearDown(self):
		""" tear down for test """
		# print('Tear down for [' + self.shortDescription() + ']')
		pass
		
		
	# insert
	def test_01_insert(self):
		""" 01. NEW KEY INSERTION """
		result = SolutionTestCase.TEST_TRIE.insert('xabxac')
		result_2 = SolutionTestCase.TEST_TRIE.insert('go')
		result_3 = SolutionTestCase.TEST_TRIE.insert('golang')
		self.assertIsNone(result)
		self.assertIsNone(result_2)
		self.assertIsNone(result_3)
		
	def test_02_insert(self):
		""" 02. INSERT EXISTING KEY """
		with self.assertRaises(KeyError):
			SolutionTestCase.TEST_TRIE.insert('xabxac')
		
	def test_03_insert(self):
		""" 03. INSERT NON 'STR' KEY """
		with self.assertRaises(TypeError):
			SolutionTestCase.TEST_TRIE.insert(123)
		
	# search
	def test_04_search(self):
		""" 04. SEARCH FOR AN EXISTING KEY """
		result = SolutionTestCase.TEST_TRIE.search('xabxac')
		self.assertTrue(result[0])
		
	def test_05_search(self):
		""" 05. SEARCH FOR NON-EXISTING KEY """
		result = SolutionTestCase.TEST_TRIE.search('xabxa')
		self.assertFalse(result[0])
		
	def test_06_search(self):
		""" 06. SEARCH FOR A KEY OF TYPE NOT 'STR' """
		with self.assertRaises(TypeError):
			SolutionTestCase.TEST_TRIE.search(123)
		
	def test_07_search(self):
		""" 07. COMPARING THE KEY WITH A WORD COMPOSED OF NODE LABELS """
		result = SolutionTestCase.TEST_TRIE.search('xabxac')
		self.assertEqual(result[1], 'xabxac')
		
	# remove
	def test_08_remove(self):
		""" 08. DELETING AN EXISTING KEY """
		result = SolutionTestCase.TEST_TRIE.remove('xabxac')
		self.assertIsNone(result)
		
	def test_09_remove(self):
		""" 09. DELETING A DELETED KEY """
		with self.assertRaises(KeyError):
			SolutionTestCase.TEST_TRIE.remove('xabxac')
		
	def test_10_remove(self):
		""" 10. DELETING A NON-EXISTENT KEY """
		with self.assertRaises(KeyError):
			SolutionTestCase.TEST_TRIE.remove('abcd')
		
	def test_11_remove(self):
		""" 11. DELETING A KEY OF TYPE NOT 'STR' """
		with self.assertRaises(TypeError):
			SolutionTestCase.TEST_TRIE.remove(123)
		
	# has_prefix
	def test_12_prefix(self):
		""" 12. SEARCH FOR EXISTING PREFIX """
		result = SolutionTestCase.TEST_TRIE.has_prefix('go')
		self.assertTrue(result)
		
	def test_13_prefix(self):
		""" 13. SEARCH FOR NON-EXISTENT PREFIX """
		result = SolutionTestCase.TEST_TRIE.has_prefix('god')
		self.assertFalse(result)
		
	def test_14_prefix(self):
		""" 14. SEARCH FOR NON 'STR' PREFIX """
		with self.assertRaises(TypeError):
			SolutionTestCase.TEST_TRIE.has_prefix(123)
			
	# is_terminal
	def test_15_terminal(self):
		""" 15. CHECK 'IS_TERMINAL' IN TERMINAL/NON-TERMINAL VERTICES """
		# prefix 'go'
		result = SolutionTestCase.TEST_TRIE.root.children[ord('g') - ord('a')].children[ord('o') - ord('a')].is_terminal
		
		# prefix 'gol'
		result_2 = SolutionTestCase.TEST_TRIE.root.children[ord('g') - ord('a')].children[ord('o') - ord('a')].children[ord('l') - ord('a')].is_terminal
		
		self.assertTrue(result)
		self.assertFalse(result_2)
		
	# key
	def test_16_key(self):
		""" 16. CHECK 'KEY' IN TERMINAL/NON-TERMINAL VERTICES """
		# word 'go'
		result = SolutionTestCase.TEST_TRIE.root.children[ord('g') - ord('a')].children[ord('o') - ord('a')].key
		
		# prefix 'gol'
		result_2 = SolutionTestCase.TEST_TRIE.root.children[ord('g') - ord('a')].children[ord('o') - ord('a')].children[ord('l') - ord('a')].key
		
		self.assertEqual(result, 'go')
		self.assertIsNone(result_2)
		

if __name__ == '__main__':
	unittest.main()

