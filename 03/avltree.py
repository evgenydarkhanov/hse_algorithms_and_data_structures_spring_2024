from __future__ import annotations
from typing import Optional
import pickle


class KeyNotFoundException(Exception):
	pass


class EmptyTreeException(Exception):
	pass


class AVLNode:
	"""
	имплементация узла АВЛ-дерева для решения задачи
	ожидатся, что каждом узле ключ: str, значение: Optional[int]
	"""
	def __init__(self, key: str, value: Optional[int]=None, 
				left: Optional[AVLNode]=None,
				right: Optional[AVLNode]=None, height: int=1):
		self.key = key
		self.value = value
		self.left = left
		self.right = right
		self.height = height


class AVLTree:
	def __init__(self) -> None:
		"""
		имплементация АВЛ-дерева для решения задачи
		def func_name(...) - для взаимодействия с экземпляром класса
		def _func_name(...) - для внутреннего пользования
		"""
		self.number_of_elements: int = 0
		self.root: Optional[AVLNode]=None

	def get_number_of_elements(self) -> int:
		return self.number_of_elements

	def _height(self, node: Optional[AVLNode]) -> int:
		if node is None:
			return 0
		return node.height

	def _balance_factor(self, node) -> int:
		if node is None:
			return 0
		return self._height(node.left) - self._height(node.right)

	def _balance(self, node) -> Optional[AVLNode]:
		""" балансировка поворотами """
		if node is None:
			return None

		node.height = 1 + max(self._height(node.left), self._height(node.right))
		balance_factor = self._balance_factor(node)

		if balance_factor > 1:
			if self._balance_factor(node.left) < 0:
				node.left = self._rotate_left(node.left)
			return self._rotate_right(node)

		if balance_factor < -1:
			if self._balance_factor(node.right) > 0:
				node.right = self._rotate_right(node.right)
			return self._rotate_left(node)

		return node

	def _rotate_right(self, q) -> AVLNode:
		""" малый правый поворот """
		p = q.left
		T = p.right
		p.right = q
		q.left = T
		q.height = 1 + max(self._height(q.left), self._height(q.right))
		p.height = 1 + max(self._height(p.left), self._height(p.right))
		return p

	def _rotate_left(self, p) -> AVLNode:
		""" малый левый поворот """
		q = p.right
		T = q.left
		q.left = p
		p.right = T
		p.height = 1 + max(self._height(p.left), self._height(p.right))
		q.height = 1 + max(self._height(q.left), self._height(q.right))
		return q

	def _search(self, search_key):
		""" поиск по ключу: для внутреннего пользования """
		# кажется, что здесь получается слишком жёсткая привязка к типам данных
		# с другой стороны: "ключу, представляющему из себя регистронезависимую последовательность букв английского алфавита"
		if not isinstance(search_key, str):
			raise TypeError("key must be 'str'")
			
		if self.number_of_elements == 0:
			raise EmptyTreeException('EmptyTreeException')
		
		search_key = search_key.lower()     # регистронезависимость
		current_node = self.root
		while current_node.key != search_key:
			if current_node.key > search_key:
				current_node = current_node.left
			else:
				current_node = current_node.right
			if current_node is None:
				return None
		return current_node

	def search(self, search_key) -> Optional[AVLNode]:
		""" поиск по ключу """
		try:
			result = self._search(search_key)
			if result is None:
				return None
			else:
				return result
		except EmptyTreeException:
			return None
		except TypeError as te:
			raise TypeError(f'{te}')

	def _insert(self, node, insert_key, insert_value) -> AVLNode:
		""" вставка по ключу: для внутреннего пользования """
		if node is None:
			return AVLNode(key=insert_key, value=insert_value)
		if insert_key < node.key:
			node.left = self._insert(node.left, insert_key, insert_value)
		else:
			node.right = self._insert(node.right, insert_key, insert_value)
		return self._balance(node)

	def insert(self, insert_key, insert_value=None) -> Optional[AVLNode]:
		""" вставка по ключу """
		try:
			search_result = self._search(insert_key)    # проверка типов и наличия ключа в дереве
			insert_key = insert_key.lower()		# регистронезависимость
			if search_result is None:
				self.root = self._insert(self.root, insert_key, insert_value)
				self.number_of_elements += 1
				return None
			else:
				return True
		except EmptyTreeException:  # случай с корнем
			self.root = self._insert(self.root, insert_key, insert_value)
			self.number_of_elements += 1
			return None
		except TypeError as te:
			raise TypeError(f'{te}')

	def _remove(self, node, remove_key, parent=None):
		""" удаление по ключу: для внутреннего пользования """
		if node is None:
			return None
		if remove_key < node.key:
			node.left = self._remove(node.left, remove_key, node)
		elif remove_key > node.key:
			node.right = self._remove(node.right, remove_key, node)
		else:
			q = node.left
			r = node.right
			if r is None:
				if parent is not None:
					if parent.left == node:
						parent.left = q
					else:
						parent.right = q
					return q

			min_node_parent = node
			min_node = r
			while min_node.left is not None:
				min_node_parent = min_node
				min_node = min_node.left

			if min_node_parent != node:
				min_node_parent.left = min_node.right
				min_node.right = r

			min_node.left = q
			return self._balance(min_node)

		return self._balance(node)

	def remove(self, remove_key):
		""" удаление по ключу """
		try:
			remove_result = self._search(remove_key)    # проверка типов и наличия ключа в дереве
			if remove_result is None:
				raise KeyNotFoundException('KeyNotFoundException')
			remove_key = remove_key.lower()		# регистронезависимость
			self.root = self._remove(self.root, remove_key)
			self.number_of_elements -= 1
		except KeyNotFoundException:
			raise KeyNotFoundException('KeyNotFoundException')
		except TypeError as te:
			raise TypeError(f'{te}')
			
	def save(self, file_path):
		try:
			with open(file_path, 'wb') as file:
				pickle.dump(self.root, file)
			return True
		except pickle.PickleError as pe:
			raise pickle.PickleError(f'{pe}')
		except pickle.PicklingError as pge:
			raise pickle.PicklingError(f'{pge}')
		except Exception as e:
			raise Exception(f'{e}')

	def load(self, file_path):
		try:
			with open(file_path, 'rb') as file:
				self.root = pickle.load(file)
			return True
		except pickle.UnpicklingError as ue:
			raise pickle.UnpicklingError(f'ue')
		except Exception as e:
			raise Exception(f'{e}')

