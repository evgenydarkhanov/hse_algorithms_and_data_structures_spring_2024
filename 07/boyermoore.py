from typing import Optional


def shift_hashmap(pattern: list[str]):
	m = len(pattern)
	hashmap = {}
	hashmap[pattern[-1]] = m
	for i in range(m - 1):
		hashmap[pattern[i]] = m - i - 1
		
	return hashmap
	
	
def boyer_moore_search(text: list[str], pattern: list[str]) -> Optional[list[int]]:
	n = len(text)
	m = len(pattern)
	if m > n:
		return None
		
	# хеш-таблица сдвигов для эвристики плохого символа
	hashmap = shift_hashmap(pattern)
	entries = []
	
	# скользим по тексту слева направо
	i = 0
	while i < (n - m + 1):
		j = m - 1
		
		# скользим по образцу справа налево
		while j >= 0 and pattern[j] == text[i + j]:
			j -= 1
			if j == 0:
				entries.append(i + j + 1)	# нумерация начинается с единицы, поэтому везде индекс += 1
				
		# при несовпадении делаем сдвиг согласно значению из таблицы
		i += hashmap.get(text[i + j], m)
		
	return entries or None

