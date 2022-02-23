class Node:
	def __init__(self, data, parent):
		self.data = data
		self.leftChild = None
		self.rightChild = None
		self.parent = parent

class BinarySearchTree:
	def __init__(self):
		self.root = None

	# we start at root node. If the data we want to insert is greater than the root node we go to the right, if it is smaller, we go to the left ...
	def insert(self, data):
		if self.root is None:
			self.root = Node(data, None)
		else:
			self.insert_node(data, self.root)

	# O(logN) BUT if tree is balanced (left subtree contains approx same amt of items than right subtree
	# O(N) if imbalanced
	def insert_node(self, data, node):
		# go to left but check if the data is already present
		if data < node.data:
			# node has left child
			if node.leftChild:
				self.insert_node(data, node.leftChild)
			else:
				node.leftChild = Node(data, node)
		# right subtree
		else:
			if node.rightChild:
				self.insert_node(data, node.rightChild)
			else:
				node.rightChild = Node(data, node)

	def traverse(self):
		if self.root is not None:
			self.traverse_in_order(self.root)

	def get_max_value(self):
		if self.root:
			return self.get_max(self.root)

	# largest = rightmost item in BST
	# minimum = leftmost item in BST

	# recursive solution
	def get_max(self, node):
		if node.rightChild:
			return self.get_max(node.rightChild)
		return node.data

	# iterative solution
	def get_max2(self, node):
		actual = self.root
		while actual.rightChild is not None:
			actual = actual.rightChild
		return actual.data

	def get_min_value(self):
		if self.root:
			return self.get_min(self.root)

	def get_min(self, node):
		if node.leftChild:
			return self.get_min(node.leftChild)
		return node.data

	# left, root, right
	def traverse_in_order(self, node):
		if node.leftChild:
			self.traverse_in_order(node.leftChild)
		print('%s' % node.data)
		if node.rightChild:
			self.traverse_in_order(node.rightChild)

	def remove_node(self, data, node):
		if node is None:
			return
		if data < node.data:
			self.remove_node(data, node.leftChild)
		elif data > node.data:
			self.remove_node(data, node.rightChild)
		else:
			# Case 1) remove leaf node
			# we have to find the item itself + delete it or set it to NULL
			# ~ O(logN) find operation + O(1) deletion = O(logN)
			if node.leftChild is None and node.rightChild is None:
				print("Removing a leaf node %d" % node.data)
				# get parent
				parent = node.parent
				# check if node is left child or right child
				if parent is not None and parent.leftChild == node:
					parent.leftChild = None # parent's left child is removed
				if parent is not None and parent.rightChild == node:
					parent.rightChild = None # parent's right child is removed
				if parent is None: # if node is root
					self.root = None
				del node
			# Case 2) Single left/right child
			# we want to get rid of node that has a single child, we just have to update the references
			elif node.leftChild is None and node.rightChild is not None: #single right child
				print("Removing a node with single right child")
				parent = node.parent
				if parent is not None:
					if parent.leftChild == node:
						parent.leftChild = node.rightChild #rightChild because we remove node with single right child
					if parent.rightChild == node:
						parent.rightChild = node.rightChild
					else: # node is root node
						self.root = node.rightChild
					node.rightChild.parent = parent
					del node
			elif node.rightChild is None and node.leftChild is not None: # single left child
				print("Removing a node with single left child")
				parent = node.parent
				if parent is not None:
					if parent.leftChild == node:
						parent.leftChild = node.leftChild
					if parent.rightChild == node:
						parent.rightChild = node.leftChild #leftChild because we remove node with single left child
				else:
					self.root = node.leftChild
				node.leftChild.parent = parent
				del node
			# Case 3) Removing node with 2 children
			# We have two options: we look for the largest item in the left subtree (predecessor) OR the smallest in the right subtree (successor)
			# ex. take predecessor and swap the two nodes. then we end up at case 1 where we just have to set it to NULL
			else:
				print("Removing node with 2 children")
				predecessor = self.get_predecessor(node.leftChild) #largest item in left subtree
				temp = predecessor.data
				predecessor.data = node.data
				node.data = temp
				self.remove_node(data, predecessor)

	def get_predecessor(self,node):
		if node.rightChild:
			return self.get_predecessor(node.rightChild)
		return node

	def remove(self, data):
		if self.root is not None:
			self.remove_node(data, self.root)














# bst = BinarySearchTree()
# bst.insert(10)
# bst.insert(5)
# bst.insert(-5)
# bst.insert(1)
# bst.insert(99)
# bst.insert(34)
# bst.insert(1000)
# print('max item: %d' % bst.get_max(bst.root))
# print('max item: %d' % bst.get_max2(bst.root))
# print('min item: %d' % bst.get_min(bst.root))
# bst.traverse()
#
# print()
# bst.remove(15) # not in tree, nothing happens
# bst.remove(10)
# bst.traverse()
