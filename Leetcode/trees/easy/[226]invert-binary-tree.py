# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root 
        

    def jin(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            left_node = root.left
            right_node = root.right
            root.left = right_node
            root.right = left_node
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root         



    def invertTree(self, root):
        if root:
            temp = root.right
            root.right = root.left
            root.left = temp
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root