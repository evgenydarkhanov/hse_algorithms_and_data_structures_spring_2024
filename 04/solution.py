from __future__ import annotations
from typing import Hashable, Any, Optional
import ctypes

from hashtable import Node, HashTable

import random


if __name__ == '__main__':

	hashtable = HashTable()
	test_arr = [(str(random.randint(0, 9999)), random.randint(0, 9999)) for _ in range(50)]
	
	for elem in test_arr:
		hashtable[elem[0]] = elem[1]
	
	print('test array')	
	print(f'unique keys = {len({elem[0] for elem in test_arr})}')
	print(test_arr)
	print()
	print(f'hashtable.get_size() = {hashtable.get_size()}')
	print(f'hashtable.get_capacity() = {hashtable.get_capacity()}')
	print(f'hashtable.get_load_factor() = {hashtable.get_load_factor()}')
	print('hashtable.items() =')
	print(hashtable.items())

