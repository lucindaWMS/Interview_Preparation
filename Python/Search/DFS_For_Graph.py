#DFS for Graph

from Graph import Graph

def dfs(graph, source):
	stack = []
	order = []
	stack.append(source)

	while stack:
		node = stack.pop()
		order.append(node)

		for i in graph[node]:
			#if the graph is a tree, we don't need line 16
			if i not in order and i not in stack:
				stack.append(i)

	return order

def main():
	nodes = [i for i in range(1, 9)]
	sides = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 8), (5, 8), (3, 6), (3, 7), (6, 7)]
	graph = Graph(nodes, sides)
	print(dfs(graph.sequence, 1))

if __name__ == '__main__':
	main()
