#Floyd

import math

graph = [[0, 1, 3, 1, math.inf, 9],
		[math.inf, 0, 1, 2, 3, math.inf],
		[math.inf, math.inf, 0, math.inf, math.inf, 2],
		[math.inf, math.inf, math.inf, 0, 1, math.inf],
		[math.inf, math.inf, math.inf, math.inf, 0, 6],
		[math.inf, math.inf, math.inf, math.inf, math.inf, 0]]

for i in range(len(graph)):
	for j in range(len(graph)):
		for k in range(len(graph)):
			if graph[i][j] > graph[i][k] + graph[k][j]:
				graph[i][j] = graph[i][k] + graph[k][j]

print (graph)