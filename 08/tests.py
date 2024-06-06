import floydwarshall
from scipy.sparse.csgraph import floyd_warshall
import unittest


def lists_are_equal(lst1, lst2):
	for i in range(len(lst2)):
		for j in range(len(lst2)):
			# в scipy не используется float('inf')
			if lst2[i][j] == -9223372036854775808:
				lst2[i][j] = float('inf')
				
	return lst1 == lst2


class SolutionTestCase(unittest.TestCase):


	@classmethod
	def setUpClass(cls):
		""" set up for class """
		print("FLOYD-WARSHALL TESTS")
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
		""" 01. UNDIRECTED GRAPH WITH POSITIVE EDGES """
		MAX = float('inf')
		graph = [[0, 2, MAX, 3, 1, MAX, MAX, 10],
				 [2, 0, 4, MAX, MAX, MAX, MAX, MAX],
				 [MAX, 4, 0, MAX, MAX, MAX, MAX, 3],
				 [3, MAX, MAX, 0, MAX, MAX, MAX, 8],
				 [1, MAX, MAX, MAX, 0, 2, MAX, MAX],
				 [MAX, MAX, MAX, MAX, 2, 0, 3, MAX],
				 [MAX, MAX, MAX, MAX, MAX, 3, 0, 1],
				 [10, MAX, 3, 8, MAX, MAX, 1, 0]]
				 
		dist_1 = floydwarshall.floyd_warshall(graph)
		dist_2 = floyd_warshall(graph, directed=False).astype('int').tolist()
		self.assertTrue(lists_are_equal(dist_1, dist_2))
		
	def test_02(self):
		""" 02. DIRECTED GRAPH WITH POSITIVE EDGES """
		MAX = float('inf')
		graph = [[0, 5, MAX, 10],
				 [MAX, 0, 3, MAX],
				 [MAX, MAX, 0, 1],
				 [MAX, MAX, MAX, 0]]
		
		dist_1 = floydwarshall.floyd_warshall(graph)
		dist_2 = floyd_warshall(graph, directed=True).tolist()
		self.assertTrue(lists_are_equal(dist_1, dist_2))
		
	def test_03(self):
		""" 03. DIRECTED GRAPH WITH NEGATIVE EDGES """
		MAX = float('inf')
		graph = [[0, MAX, -2, MAX],
				 [4, 0, 3, MAX],
				 [MAX, MAX, 0, 2],
				 [MAX, -1, MAX, 0]]
		
		dist_1 = floydwarshall.floyd_warshall(graph)
		dist_2 = floyd_warshall(graph, directed=True).tolist()
		self.assertTrue(lists_are_equal(dist_1, dist_2))


if __name__ == '__main__':
	unittest.main()

