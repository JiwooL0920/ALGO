"""
Write an efficient algorithm that's able to compare two BTSs.
The method returns true if the trees are identical (same topology with same
values in the nodes) otherwise it returns false
"""
from ADS_Udemy.BinarySearchTree.Code.BinarySearchTree import *

# task is that we want to compare BST as far as topology and matching values are concerned
# make something like in-order traversal

class TreeComparator(object):
	def compare_trees(self, node1, node2):
		# we have to check the base case
		# it may be the child of a leaf node so we have to use ==
		if not node1 or not node2:
			return node1 == node2
		# if the values within the nodes are not the same, return false
		# tree topology is not the same
		if node1.data is not node2.data:
			return False
		# the left subtree values AND the right subtree values must match as well
		return self.compare_trees(node1.leftChild, node2.leftChild) and self.compare_trees(node1.rightChild, node2.rightChild)




if __name__ == "__main__":
	bst1 = BinarySearchTree()
	bst1.insert(10)
	# bst1.insert(13)
	# bst1.insert(2)
	# bst1.insert(14)

	bst2 = BinarySearchTree()
	bst2.insert(10)
	# bst2.insert(13)
	# bst2.insert(2)
	# bst2.insert(14)

	comparator = TreeComparator()
	print(comparator.compare_trees(bst1.root, bst2.root))