def floyd_warshall(graph: list) -> list:
	""" алгоритм Флойда-Уоршелла для графа, представленного матрицей смежности """
	num_vertices = len(graph)
	dist = [[float('inf') for i in range(num_vertices)] for _ in range(num_vertices)]
	
	for i in range(num_vertices):
		for j in range(num_vertices):
			if i == j:
				dist[i][j] = 0
			elif graph[i][j] != 0:
				dist[i][j] = graph[i][j]
				
	for k in range(num_vertices):
		for i in range(num_vertices):
			for j in range(num_vertices):
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
	
	return dist

