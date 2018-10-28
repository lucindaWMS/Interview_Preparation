#Construct a graph class

class Graph():

	def __init__(self, nodes, sides):
		#Key is node, value is adjacent nodes
		self.sequence = {}
		#Temporary variable, store the adjacent nodes of a given node
		self.side = []
		for node in nodes:
			for side in sides:
				start, end = side
				if node == start:
					self.side.append(end)
				elif node == end:
					self.side.append(start)
			self.sequence[node] = self.side
			self.side = []
	