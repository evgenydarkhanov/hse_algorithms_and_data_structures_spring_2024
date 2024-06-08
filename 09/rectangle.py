def zero_one_swap(matrix) -> None:
	""" меняет 0 на 1, 1 на 0 """
	for i in range(len(matrix)):
		for j in range(len(matrix[1])):
			matrix[i][j] = 1 - matrix[i][j]
			
			
def find_rectangle_in_histogram(hist: list) -> int:
	""" считает площадь наибольшего прямоугольника под гистограммой """
	area = 0
	stack = []
	i = 0
	while i < len(hist):
		if not stack or hist[stack[-1]] <= hist[i]:
			stack.append(i)
			i += 1
		else:
			top = stack.pop()
			width = i if not stack else i - stack[-1] - 1
			area = max(area, hist[top] * width)
	while stack:
		top = stack.pop()
		width = i if not stack else len(hist) - stack[-1] - 1
		area = max(area, hist[top] * width)
	return area
	

def make_hist(row_1, row_2, m) -> list[int]:
	""" делает гистограммы из строк матрицы """
	for i in range(m):
		row_2[i] = row_1[i] + 1 if row_2[i] != 0 else row_2[i]

			
def find_rectangle_in_matrix(matrix: list[list]) -> int:
	""" находит наибольший прямоугольник из 0 с помощью гистограмм """
	zero_one_swap(matrix)
	hist = matrix[0]
	m = len(hist)
	area = find_rectangle_in_histogram(hist)
	
	for row in matrix[1:]:
		make_hist(hist, row, m)
		area = max(area, find_rectangle_in_histogram(row))
		hist = row
			
	return area
	

if __name__ == "__main__":
	matrix = [
				[0, 1, 0, 1, 1],
				[1, 0, 0, 0, 1],
				[0, 1, 0, 0, 0],
				[1, 1, 0, 1, 1]
		]
	for row in matrix:
		print(row)
	print()
	print(find_rectangle_in_matrix(matrix))

