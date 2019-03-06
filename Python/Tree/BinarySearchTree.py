class BinaryTreeNode:
	def __init__(self, val = None, parent = None, left = None, right = None):
		self.val = val
		self.parent = parent
		self.left = left
		self.right = right

class BinarySearchTree:
	def __init__(self):
		self.root = None
		self.size = 0
		self.depth = 0

	def insert(self, node):
		if node == None:
			return
		if self.root == None:
			self.root = node
			self.size += 1
			self.depth = 1
			return

		temp_node = self.root
		temp_depth = 1

		while True:
			temp_depth += 1
			if node.val <= temp_node.val:
				if temp_node.left == None:
					node.parent = temp_node
					temp_node.left = node
					self.size += 1
					self.depth = max(temp_depth, self.depth)
					break
				else:
					temp_node = temp_node.left
			elif node.val > temp_node.val:
				if temp_node.right == None:
					node.parent = temp_node
					temp_node.right = node
					self.size += 1
					self.depth = max(temp_depth, self.depth)
					break
				else:
					temp_node = temp_node.right

	def find(self, val):
		if val == None or self.root == None:
			print('Not Found')
			return
		temp_node = self.root

		while True:
			if val == temp_node.val:
				print('Find it', val)
				break
			elif val < temp_node.val:
				if temp_node.left == None:
					print('Not found')
					return
				else:
					temp_node = temp_node.left
			else:
				if temp_node.right == None:
					print('Not found')
					return
				else:
					temp_node = temp_node.right

	def preOrder(self, node):
		if node == None:
			return
		print(node.val)
		self.preOrder(node.left)
		self.preOrder(node.right)

	def inOrder(self, node):
		if node == None:
			return
		self.inOrder(node.left)
		print(node.val)
		self.inOrder(node.right)

	def postOrder(self, node):
		if node == None:
			return
		self.postOrder(node.left)
		self.postOrder(node.right)
		print(node.val)

	def levelOrder(self, node):
		if node == None:
			return
		queue = [node]
		while queue:
			temp_node = queue.pop(0)
			print(temp_node.val)
			if temp_node.left:
				queue.append(temp_node.left)
			if temp_node.right:
				queue.append(temp_node.right)

	def get_depth(self, node):
		return self.depth

if __name__ == '__main__':
	tree = BinarySearchTree()
	tree.insert(BinaryTreeNode(5))
	tree.insert(BinaryTreeNode(2))
	tree.insert(BinaryTreeNode(-3))
	tree.insert(BinaryTreeNode(4))
	tree.insert(BinaryTreeNode(3))
	tree.insert(BinaryTreeNode(6))
	tree.insert(BinaryTreeNode(-1))
	tree.insert(BinaryTreeNode(7))

	tree.preOrder(tree.root)

	tree.inOrder(tree.root)

	tree.postOrder(tree.root)

	tree.levelOrder(tree.root)

	tree.find(-3)
	tree.find(99)
	print(tree.get_depth(tree.root))


