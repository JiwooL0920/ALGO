class Solution(object):
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root:
			return []

		queue = [root]
		res = []

		while queue:
			currLevel = []
			nextLevel = []
			for node in queue:
				currLevel.append(node.val)
				if node.left:
					nextLevel.append(node.left)
				if node.right:
					nextLevel.append(node.right)
			res.append(currLevel)
			queue = nextLevel

		return res
