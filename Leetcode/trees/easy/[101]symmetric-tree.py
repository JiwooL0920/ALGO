# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
	def isSymmetric2(self, left, right):
		if not left and not right:
			return True
		if not left or not right:
			return False
		else:
			return left.val == right.val and self.isSymmetric2(left.left, right.right) and self.isSymmetric2(left.right,
																											 right.left)

	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		return self.isSymmetric2(root, root)

