# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
	def inorderTraversal(self, root):
		if root:
			return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
		else:
			return []

	def isValidBST_bad(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		inorder = self.inorderTraversal(root)
		return all(inorder[i] < inorder[i + 1] for i in range(len(inorder) - 1))


