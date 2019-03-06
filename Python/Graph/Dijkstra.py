# Dijkstra 
import math
def dijkstra(graph, source):

	if not graph:
		return None
	#All nodes in the graph
	nodes = []
	for i in range(len(graph)):
		nodes.append(i)
	#The node whose shortest path has been found will be put into this set
	visited = []
	#Put the source node into the visited set
	if source in nodes:
		visited.append(source)
		nodes.remove(source)
	else:
		return None
	#Record the distance between source node to other nodes
	distance = {source:0}
	#Initialize the distance between node to other nodes by edges in graph
	for i in nodes:
		distance[i] = graph[source][i]
	# record the shortest path from source node to other nodes
	path = {source:{source:[]}}

	k = source
	pre = source

	while nodes:
		mid_distance = float("inf")
		for v in visited:
			for d in nodes:
				new_distance = graph[source][v] + graph[v][d]
				if new_distance < mid_distance:
					mid_distance = new_distance
					graph[source][d] = new_distance
					k = d
					pre = v
		distance[k] = mid_distance
		path[source][k] = [i for i in path[source][pre]]
		path[source][k].append(k)

		visited.append(k)
		nodes.remove(k)

		print(visited, nodes)
	return distance, path

if __name__ == '__main__':
	graph_list = [[0, 2, 1, 4, 5, 1],
				[1, 0 , 4, 2, 3, 4],
				[2, 1, 0, 1, 2, 4],
				[3, 5, 2, 0, 3, 3],
				[2, 4, 3, 4, 0, 1],
				[3, 4, 7, 3, 1, 0]]
	new_graph_list = [[0, 1, 3, 1, math.inf, 9],
					[math.inf, 0, 1, 2, 3, math.inf],
					[math.inf, math.inf, 0, math.inf, math.inf, 2],
					[math.inf, math.inf, math.inf, 0, 1, math.inf],
					[math.inf, math.inf, math.inf, math.inf, 0, 6],
					[math.inf, math.inf, math.inf, math.inf, math.inf, 0]]
	distance, path = dijkstra(new_graph_list, 0)
	print(distance, path)
