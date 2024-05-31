from typing import Optional
import boyermoore


def data_opening_preprocessing(datapath):
	text = []
	
	with open(datapath, 'r', encoding='utf-8') as file:
		pattern = file.readline().lower().split()
		print(*pattern)
		for line in file.readlines():
			print(line.rstrip())
			text.extend(line.lower().split())
			
	return pattern, text

	
if __name__ == '__main__':
	DATAPATH = './example.txt'
	pattern, text = data_opening_preprocessing(DATAPATH)
	result = boyermoore.boyer_moore_search(text, pattern)
	for elem in result:
		print(f'{1}, {elem}')

