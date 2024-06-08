from rectangle import zero_one_swap, find_rectangle_in_histogram, make_hist, find_rectangle_in_matrix
import random
import unittest


def generate_random_binary_matrix():
	n = random.randint(1, 50)
	m = random.randint(1, 50)
	matrix = [[random.randint(0, 1) for _ in range(m)] for _ in range(n)]
	return matrix


class SolutionTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		""" set up for class """
		print("RECTANGLE AREA TESTS")
		print("====================")
		
	@classmethod
	def tearDownClass(cls):
		""" tear down for class """
		print("====================")
		
	def setUp(self):
		""" set up for test """
		print('\n')
		# print('Set up for [' + self.shortDescription() + ']')

	def tearDown(self):
		""" tear down for test """
		# print('Tear down for [' + self.shortDescription() + ']')
		pass
		
	def test_01(self):
		""" 01. ZERO MATRIX """
		matrix = [
					[0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0]
			]
				 
		self.assertEqual(36, find_rectangle_in_matrix(matrix))
		
	def test_02(self):
		""" 02. MATRIX WITH NO ZEROS """
		matrix = [
					[1, 1, 1],
					[1, 1, 1],
					[1, 1, 1]
			]
				 
		self.assertEqual(0, find_rectangle_in_matrix(matrix))
		
	def test_03(self):
		""" 03. MATRIX WITH ONE ZERO """
		matrix = [
					[1, 1, 1],
					[1, 0, 1],
					[1, 1, 1]
			]
				 
		self.assertEqual(1, find_rectangle_in_matrix(matrix))
		
	def test_04(self):
		""" 04. RING MATRIX """
		matrix = [
					[0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0],
					[0, 0, 1, 1, 0, 0],
					[0, 0, 1, 1, 0, 0],
					[0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0]
			]
				 
		self.assertEqual(12, find_rectangle_in_matrix(matrix))
		
	def test_05(self):
		""" 05. RANDOM MATRIX """
		matrix = generate_random_binary_matrix()
		for row in matrix:
			print(row)
		print()
		print(f'area = {find_rectangle_in_matrix(matrix)}')
		self.assertTrue(True)


if __name__ == '__main__':
	unittest.main()

