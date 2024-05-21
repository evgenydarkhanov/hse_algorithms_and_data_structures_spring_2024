from __future__ import annotations
from typing import Optional
import pickle

from avltree import KeyNotFoundException, EmptyTreeException, AVLNode, AVLTree

import unittest
import random


test_arr = [(str(i), i) for i in range(100)]
random.shuffle(test_arr)

test_tree = AVLTree()
for elem in test_arr:
	test_tree.insert(insert_key=elem[0], insert_value=elem[1])
	

class SolutionTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		"""Set up for class"""
		print("AVL TREE DICTIONARY TESTS")
		print("=========================")
		
	@classmethod
	def tearDownClass(cls):
		"""Tear down for class"""
		print("=========================")
		
	def setUp(self):
		"""Set up for test"""
		print('\n')
		#print('Set up for [' + self.shortDescription() + ']')

	def tearDown(self):
		#print('Tear down for [' + self.shortDescription() + ']')
		pass

		
	# поиск
	def test_01_search_exists(self):
		"""01. SEARCH BY EXISTING KEY"""
		random_key = random.randint(0, 99)
		result = test_tree.search(str(random_key))
		self.assertEqual(random_key, result.value)
		
	def test_02_search_not_exists(self):
		"""02. SEARCH FOR A NON-EXISTENT KEY"""
		result = test_tree.search(str(200))
		self.assertIsNone(result)
		
	def test_03_search_key_datatype(self):
		"""03. SEARCH BY KEY OF ANOTHER DATA TYPE"""
		random_key = random.randint(0, 99)
		with self.assertRaises(TypeError):
			result = test_tree.search(random_key)
		
	# вставка
	def test_04_insert_exists(self):
		"""04. INSERT BY EXISTENT KEY"""
		result = test_tree.insert(str(99), 99)
		self.assertTrue(result)
		
	def test_05_insert_not_exists(self):
		"""05. INSERT BY NON-EXISTING KEY"""
		result = test_tree.insert(str(105), 105)
		self.assertIsNone(result)
		
	def test_06_insert_key_datatype(self):
		"""06. INSERT BY KEY OF ANOTHER DATA TYPE"""
		with self.assertRaises(TypeError):
			result = test_tree.insert(101, 101)
		
	def test_07_insert_non_value(self):
		"""07. INSERTING A KEY WITHOUT A VALUE"""
		result = test_tree.insert(str(102))
		self.assertIsNone(result)
		
	# удаление
	def test_08_remove_key_datatype(self):
		"""08. DELETING BY KEY OF ANOTHER DATA TYPE"""
		with self.assertRaises(TypeError):
			result = test_tree.remove(101, 101)
		
	def test_09_remove_leaf(self):
		"""09. DELETING LEAF KEY"""
		result = test_tree.remove(str(105))
		self.assertIsNone(result)
		
	def test_10_remove_vertex_one_descendant(self):
		"""10. DELETING A VERTEX KEY WITH ONE DESCENDANT"""
		result = test_tree.remove(str(102))
		self.assertIsNone(result)
		
	def test_11_remove_vertex_two_descendants(self):
		"""11. DELETING A VERTEX KEY WITH TWO DESCENDANT"""
		key_to_remove = test_tree.root.left.key
		result = test_tree.remove(key_to_remove)
		self.assertIsNone(result)
		
	def test_12_remove_root(self):
		"""12. ROOT KEY REMOVAL"""
		key_to_remove = test_tree.root.key
		result = test_tree.remove(key_to_remove)
		self.assertIsNone(result)

	def test_13_remove_already_removed(self):
		"""13. DELETING A KEY OF AN ALREADY DELETED VERTEX"""
		with self.assertRaises(KeyNotFoundException):
			result = test_tree.remove(str(102))
		
	def test_14_remove_not_existed(self):
		"""14. DELETING THE KEY OF A NONEXISTENT VERTEX"""
		with self.assertRaises(KeyNotFoundException):
			result = test_tree.remove(str(200))
		
	# работа с файлами
	def test_15_saving(self):
		"""15. SAVING"""
		result = test_tree.save('./dictionary.pickle')
		self.assertTrue(result)
		
	def test_16_loading(self):
		"""16. LOADING"""
		result = test_tree.load('./dictionary.pickle')
		self.assertTrue(result)
		
if __name__ == '__main__':
	unittest.main()

