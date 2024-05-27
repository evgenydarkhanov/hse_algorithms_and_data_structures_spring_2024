from typing import Optional, Tuple


class TrieNode:
	def __init__(self, label: str, children=None,
				key: Optional[str] = None, is_terminal=False):
				
		self.label = label.lower()
		self.children = children or [None] * 26
		self.key = key
		self.is_terminal = is_terminal
		
		
class Trie:
	def __init__(self):
		self.root = TrieNode(label='')

	def insert(self, insert_key: str) -> None:
		if not insert_key:
			return None
		if not isinstance(insert_key, str):
			raise TypeError('the insertion key must be str')
		if self.search(insert_key)[0]:
			raise KeyError('the insertion key exists')
			
		else:
			node = self.root
		
			for char in insert_key:
				index = ord(char) - ord('a')
				if node.children[index] is None:
					node.children[index] = TrieNode(label=char)
				node = node.children[index]
			node.key = insert_key
			node.is_terminal = True

	def search(self, search_key: str) -> Tuple[bool, str]:
		if not search_key:
			return None
		if not isinstance(search_key, str):
			raise TypeError('the search key must be str')

		node = self.root
		word = node.label

		for char in search_key:
			index = ord(char) - ord('a')
			if node.children[index] is None:
				return (False, '')
			node = node.children[index]
			word += node.label
		if not node.is_terminal:
			return (False, '')
		return (True, word)

	def remove(self, remove_key: str) -> None:
		if not remove_key:
			return None
		if not isinstance(remove_key, str):
			raise TypeError('the removal key must be str')

		node = self.root
		word = node.label

		for char in remove_key:
			index = ord(char) - ord('a')
			node = node.children[index]
			if node is None:
				raise KeyError('there is no such key to remove')
			if node.label:
				word += node.label
			else:
				raise KeyError('there is no such key to remove')
			if word == remove_key and node.is_terminal: 
				node.is_terminal = False
			elif word == remove_key and not node.is_terminal:
				raise KeyError('there is no such key to remove')

	def has_prefix(self, prefix: str) -> bool:
		if not prefix:
			return None
		if not isinstance(prefix, str):
			raise TypeError('the prefix must be str')

		node = self.root
		for char in prefix:
			index = ord(char) - ord('a')
			if not node.children[index]:
				return False
			node = node.children[index]
		return True

