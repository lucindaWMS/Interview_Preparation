#BFS for Graph

from Graph import Graph

def bfs(graph, source):
	queue = [source]
	order = []

	while queue:
		node = queue.pop(0)
		order.append(node)

		for i in graph[node]:
			if i not in queue and i not in order:
				queue.append(i)
	return order

def main():
	nodes = [i for i in range(1, 9)]
	sides = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 8), (5, 8), (3, 6), (3, 7), (6, 7)]
	graph = Graph(nodes, sides)
	print(bfs(graph.sequence, 1))

if __name__ == '__main__':
	main()
