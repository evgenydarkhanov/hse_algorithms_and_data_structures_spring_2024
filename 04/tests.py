from __future__ import annotations
from typing import Hashable, Any, Optional
import ctypes

from hashtable import Node, HashTable

import random
import unittest


def generate_arr_hashtable(length: int):
	arr = [(str(random.randint(0, 9999)), random.randint(0, 9999)) for _ in range(length)]
	table = HashTable()
	for elem in arr:
		table[elem[0]] = elem[1]
	return arr, table
	

class SolutionTestCase(unittest.TestCase):

	HASH_TABLE = HashTable()

	@classmethod
	def setUpClass(cls):
		""" set up for class """
		print("HASHTABLE TESTS")
		print("===============")
		
	@classmethod
	def tearDownClass(cls):
		""" tear down for class """
		print("================")
		
	def setUp(self):
		""" set up for test """
		print('\n')
		# print('Set up for [' + self.shortDescription() + ']')

	def tearDown(self):
		""" tear down for test """
		# print('Tear down for [' + self.shortDescription() + ']')
		pass
		
		
	# __setitem__
	def test_01_setitem(self):
		""" 01. NEW KEY: NEW VALUE """
		SolutionTestCase.HASH_TABLE[0] = '0'
		self.assertEqual('0', SolutionTestCase.HASH_TABLE[0])
		
	def test_02_setitem(self):
		""" 02. EXISTING KEY: NEW VALUE """
		SolutionTestCase.HASH_TABLE[0] = '00'
		self.assertEqual('00', SolutionTestCase.HASH_TABLE[0])
		
	def test_03_setitem(self):
		""" 03. NON-HASHABLE KEY """
		with self.assertRaises(TypeError):
			SolutionTestCase.HASH_TABLE[[0,]] = '0'
		
	# __getitem__
	def test_04_getitem(self):
		""" 04. EXISTING KEY """
		result = SolutionTestCase.HASH_TABLE[0]
		self.assertEqual('00', result)
		
	def test_05_getitem(self):
		""" 05. NON-EXISTENT KEY """
		with self.assertRaises(KeyError):
			result = SolutionTestCase.HASH_TABLE[1]
		
	def test_06_getitem(self):
		""" 06. NON-HASHABLE KEY """
		with self.assertRaises(TypeError):
			result = SolutionTestCase.HASH_TABLE[[0,]]
		
	# get_load_factor()
	def test_07_load_factor(self):
		""" 07. ALWAYS < 0.75 """
		_, table_1 = generate_arr_hashtable(10)
		_, table_2 = generate_arr_hashtable(100)
		_, table_3 = generate_arr_hashtable(1000)
		load_factors = table_1.get_load_factor(), table_2.get_load_factor(), table_3.get_load_factor()
		self.assertTrue(all([x < 0.75 for x in load_factors]))
		
	# get_size()
	def test_08_size(self):
		""" 08. EQUAL TO THE NUMBER OF INSERTED UNIQUE KEYS """
		arr_1, table_1 = generate_arr_hashtable(10)
		arr_2, table_2 = generate_arr_hashtable(100)
		arr_3, table_3 = generate_arr_hashtable(1000)
		unique_keys = len({elem[0] for elem in arr_1}), len({elem[0] for elem in arr_2}), len({elem[0] for elem in arr_3})
		sizes = table_1.get_size(), table_2.get_size(), table_3.get_size()
		nums = zip(unique_keys, sizes)
		self.assertTrue(all([elem[0] == elem[1] for elem in nums]))
		
	# get_capacity()
	def test_09_capacity(self):
		""" 09. INCREMENTS DURING OPERATION """
		table = HashTable()
		capacities = []
		for i in range(1, 49):
			table[str(i)] = i
			if i % 16 == 0:
				capacities.append(table.get_capacity())
		bools = [capacities[i] > capacities[i-1] for i in range(1, 3)]
		self.assertTrue(all(bools))
		
	# clear()
	def test_10_clear(self):
		""" 10. RETURNS AN EMPTY TABLE WITH PRESERVED CAPACITY AND SIZE == 0 """
		capacity = SolutionTestCase.HASH_TABLE.get_capacity()
		SolutionTestCase.HASH_TABLE.clear()
		self.assertEqual((0, capacity), (SolutionTestCase.HASH_TABLE.get_size(), SolutionTestCase.HASH_TABLE.get_capacity()))
		
	# items()
	def test_11_items(self):
		""" 11. LIST LENGTH IS EQUAL TO THE NUMBER OF INSERTED UNIQUE KEYS """
		arr, table = generate_arr_hashtable(100)
		unique_keys = len({elem[0] for elem in arr})
		len_items = len(table.items())
		self.assertEqual(unique_keys, len_items)
		
	# rehashing
	def test_12_rehashing(self):
		""" 12. DO NOT LOSE ITEMS """
		arr, table = generate_arr_hashtable(1000)
		unique_keys = len({elem[0] for elem in arr})
		size = table.get_size()
		self.assertEqual(unique_keys, size)
		

if __name__ == '__main__':
	unittest.main()

