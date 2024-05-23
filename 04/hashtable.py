from __future__ import annotations
from typing import Hashable, Any, Optional
import ctypes


class Node:
	""" узел односвязного списка для хеш-таблицы """
	def __init__(self, key: Hashable,
				 value: Any = None,
				 next: Optional[Node] = None):
		self.key = key
		self.value = value
		self.next = next
		

class HashTable:
	def __init__(self, capacity: int = 16) -> None:
		self._capacity: int = capacity
		self._size: int = 0
		self.default_load_factor = 0.75
		self._table: ctypes.Array = self._make_table(self._capacity)
		
	@staticmethod
	def _make_table(capacity: int):
		table: ctypes.Array = (capacity * ctypes.py_object)()
		for i in range(capacity):
			table[i] = None
		return table
		
	def get_size(self) -> int:
		return self._size
		
	def get_capacity(self) -> int:
		return self._capacity
		
	def get_load_factor(self) -> float:
		return self._size / self._capacity
		
	def _get_index(self, key: Hashable) -> int:
		index = hash(key) % self._capacity
		return index
		
	def _rehashing(self):
		""" увеличение размера таблицы """
		old_table = self._table
		self._capacity *= 2
		self._size = 0
		self._table: ctypes.Array = self._make_table(self._capacity)
		
		for elem in old_table:
			node = elem
			while node:
				self.__setitem__(node.key, node.value)
				node = node.next
		
	def __getitem__(self, key: Hashable):
		""" получение значения по ключу """
		try:
			index = self._get_index(key)
			node = self._table[index]
		
			while node:
				if node.key == key:
					return node.value
				node = node.next
		
			raise KeyError(f'key: {key} not found')
			
		except TypeError as te:
			raise TypeError('unhashable type: {type(key)}')
		
	def __setitem__(self, key: Hashable, value: Any):
		""" установка значения по ключу """
		try:
			# новый ключ, новое значение
			index = self._get_index(key)
			if self._table[index] is None:
				self._table[index] = Node(key, value)
				self._size += 1
			else:
				# существующий ключ, новое значение
				node = self._table[index]
				while node:
					if node.key == key:
						node.value = value
						return
					node = node.next
				else:
					# коллизия
					self._table[index] = Node(key, value, next=self._table[index])
					self._size += 1
				
			if self.get_load_factor() >= self.default_load_factor:
				self._rehashing()
				
		except TypeError as te:
			raise TypeError('unhashable type: {type(key)}')
			
	def clear(self):
		self._size = 0
		self._table: ctypes.Array = self._make_table(self._capacity)
		
	def items(self):
		""" пары ключ-значение """
		items = []
		for elem in self._table:
			node = elem
			while node:
				items.append((node.key, node.value))
				node = node.next
		return items
		
	def __str__(self) -> str:
		if self._size != 0:
			out = '{'
			for elem in self._table:
				if elem:
					node = elem
					while node:
						out += str(node.key) + ': ' + str(node.value) + ', '
						node = node.next
			out = out[:-2] + '}'
		else:
			out = '{}'
		return out

