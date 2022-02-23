class Node:
	# height = max(left child's height, right child's height) + 1
	# height of a node is the longest path from the actual node to a leaf node
	# the height of a NULL node is -1; leaf nodes have height 0
	def __init__(self, data, parent):
		self.data = data
		self.left_node = None
		self.right_node = None
		self.parent = parent
		self.height = 0


class AVLTree:
	def __init__(self):
		# we can access the root node exclusively
		self.root = None

	def remove(self, data):
		if self.root:
			self.remove_node(data, self.root)

	def remove_node(self, data, node):
		# base case
		if node is None:
			return
		# case 1) item is in left subtree
		if data < node.data:
			self.remove_node(data, node.left_node)
		# case 2) item is in right subtree
		elif data > node.data:
			self.remove_node(data, node.right_node)
		# Case 3) we found the node we want to remove
		else:
			# case 1) if node is a leaf node
			if node.left_node is None and node.right_node is None:
				print("Removing a leaf node %d" % node.data)
				parent = node.parent
				if parent is not None and parent.left_node == node: # left child of its parent
					parent.left_node = None
				if parent is not None and parent.right_node == node: # right child
					parent.right_node = None
				if parent is None: # it is root node we want to remove
					self.root = None
				del node
				# after every insertion we have to check whether the AVL properties are violated
				self.handle_violation(parent)
			# case 2) if node has a single child
			elif node.left_node is None and node.right_node is not None:
				print("Removing a node with single right child")
				parent = node.parent
				if parent is not None: # node is not root node
					if parent.left_Node == node: # decide if node we want to remove is left child or right child
						parent.left_node = node.left_node
					if parent.rightChild == node:
						parent.right_node = node.right_node
					else:
						self.root = node.right_node
					node.right_node.parent = parent
					del node
					# after every deletion we have to check whether the AVL properties are violated
				self.handle_violation(parent)
			# case 3) node we want to remove has single left child
			elif node.right_node is None and node.left_node is not None:
				print("Removing a node with single left child")
				parent = node.parent
				if parent is not None:
					if parent.left_node == node:
						parent.left_node = node.left_node
					if parent.right_node == node:
						parent.right_node = node.left_node
				else:
					self.root = node.left_node
				node.left_node.parent = parent
				del node
				self.handle_violation(parent)
			# case 4) node has 2 children
			else:
				print("Removing node with two children")
				predecessor = self.get_predecessor(node.left_node)
				temp = predecessor.data
				predecessor.data = node.data
				node.data = temp
				self.remove_node(data, predecessor) # guaranteed that we end up with first case (removing leaf)

	def get_predecessor(self, node):
		if node.right_node:
			return self.get_predecessor(node.right_node)
		return node

	def insert(self, data):
		if self.root is None: # empty tree
			self.root = Node(data, None)
		else: # find location where we would like to insert in the existing tree
			self.insert_node(data, self.root)

	def insert_node(self, data, node):
		# we have to consider the left subtree
		if data < node.data:
			# we have to check if the left node is a None
			# when left child is not a None
			if node.left_node:
				self.insert_node(data, node.left_node)
			else:
				node.left_node = Node(data, node)
				node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
		# right subtree
		else:
			# we have to check if the right node is a None
			# when right child is not a None
			if node.right_node:
				self.insert_node(data, node.right_node)
			else:
				node.right_node = Node(data, node)
				node.height = max(self.calc_height(node.right_node), self.calc_height(node.right_node)) + 1
		# after every insertion, we have to check whether the AVL properties are violated
		self.handle_violation(node)

	def calc_height(self, node):
		# node is a NULL
		if node is None:
			return -1
		return node.height

	# | hleft - hright| > 1
	# all subtrees height parameter cannot differ more than 1 (otherwise imbalanced and need rotation)
	# larger than 1 = left heavy = need right rotation
	# smaller than 1 = right heavy = need left rotation
	def calculate_balance(self, node):
		if node is None:
			return 0
		return self.calc_height(node.left_node) - self.calc_height(node.right_node)

	# checks whether the subtree is balanced with root node = node
	def violation_helper(self, node):
		balance = self.calculate_balance(node)
		# left heavy but it can be left-right heavy or left-left heavy
		if balance > 1:
			# left right heavy situation: left rotation on parent + right rotation on grandparent
			#             D
			#           /
			#         B
			#          \
			#           C
			# make left notation on node B
			#            D
			#          /
			#        C
			#      /
			#    B
			# make right rotation on node D
			#           C
			#         /   \
			#       B      D
			if self.calculate_balance(node.left_node) < 0:
				self.rotate_left(node.left_node)
			# this is the right rotation on grandparent (if left-left heavy, that's single right rotation)
			# left-left heavy
			#          A
			#        /
			#      B
		    #    /
			#  C
			# make simple right rotation
			# 	       B
	 		#        /   \
			#      C      A
			self.rotate_right(node)
		# right heavy but it can be right-left heavy or right-right heavy
		if balance < -1:
			# right-left heavy so we need to make right rotation before left rotation
			if self.calculate_balance(node.right_node) > 0:
				self.rotate_right(node.right_node)
			# left rotation
			self.rotate_left(node)

	# we always start with the node we inserted (or to be precise, the parent of the node we inserted) up to the root node
	# and in every single iteration we pose the question whether that subtree is balanced or not
	def handle_violation(self, node):
		# check the nodes from the node we have inserted up to root node
		while node is not None:
			node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
			self.violation_helper(node)
			# whenever we settle a violation (rotations) it may happen that it violates the AVL properties in other parts of the tree
			node = node.parent

	#                       D  node                                  temp_left_node     B
	#                     /  \                  rightRotate(B)                        /   \
	#  temp_left_node   B     E                 ------------>                       A      D  node
	#                  / \                      <------------                             / \
	#                 A   C                     leftRotate(B)                            C   E
	#                       t                                                           t
	# we just have to update the references which can be done in O(1) time complexity (the in-order traversal is the same)
	def rotate_right(self, node):
		print("Rotating to the right on node ", node.data)
		temp_left_node = node.left_node
		t = temp_left_node.right_node

		temp_left_node.right_node = node
		node.left_node = t

		if t is not None:
			t.parent = node

		temp_parent = node.parent
		node.parent = temp_left_node
		temp_left_node.parent = temp_parent

		# given node is a left child
		if temp_left_node.parent is not None and temp_left_node.parent.left_node == node:
			temp_left_node.parent.left_node = temp_left_node

		# given node is a right child
		if temp_left_node.parent is not None and temp_left_node.parent.right_node == node:
			temp_left_node.parent.right_node = temp_left_node

		if node == self.root:
			self.root = temp_left_node

		# recalculate height
		node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
		temp_left_node.height = max(self.calc_height(temp_left_node.left_node), self.calc_height(temp_left_node.right_node)) + 1

	def rotate_left(self, node):
		print("Rotating to the left on node ", node.data)

		temp_right_node = node.right_node
		t = temp_right_node.left_node

		temp_right_node.left_node = node
		node.right_node = t

		if t is not None:
			t.parent = node

		temp_parent = node.parent
		node.parent = temp_right_node
		temp_right_node.parent = temp_parent

		if temp_right_node.parent is not None and temp_right_node.parent.left_node == node:
			temp_right_node.parent.left_node = temp_right_node
		if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
			temp_right_node.parent.right_node = temp_right_node

		if node == self.root:
			self.root = temp_right_node

		node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
		temp_right_node.height = max(self.calc_height(temp_right_node.left_node), self.calc_height(temp_right_node.right_node)) + 1

	def traverse(self):
		if self.root is not None:
			self.traverse_in_order(self.root)

	def traverse_in_order(self, node):
		if node.left_node:
			self.traverse_in_order(node.left_node)
		l = ''
		r = ''
		p = ''

		if node.left_node is not None:
			l = node.left_node.data
		else:
			l = 'NULL'

		if node.right_node is not None:
			r = node.right_node.data
		else:
			r = 'NULL'

		if node.parent is not None:
			p = node.parent.data
		else:
			p = 'NULL'

		print("%s left: %s, right: %s, parent: %s, height: %s" % (node.data, l, r, p, node.height))

		if node.right_node:
			self.traverse_in_order(node.right_node)

if __name__ == '__main__':
	# avl = AVLTree()
	# avl.insert(32)
	# avl.insert(16)
	# avl.insert(48)
	# avl.insert(8)
	# avl.insert(24)
	# avl.insert(40)
	# avl.insert(56)
	# avl.insert(36)
	# avl.insert(44)
	# avl.insert(52)
	# avl.insert(60)
	# avl.insert(4)
	# avl.insert(58)
	# avl.insert(62)
	# avl.remove(4)
	#
	# avl.traverse()

	avl = AVLTree()
	avl.insert(5)
	avl.insert(3)
	avl.insert(10)
	avl.insert(2)
	avl.insert(4)
	avl.insert(15)

	avl.remove(15)
	avl.remove(10)



