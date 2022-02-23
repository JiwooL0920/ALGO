# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False 
        elif not root.left and not root.right:
            return root.val == targetSum 
        else:
            newSum = targetSum - root.val
            return self.hasPathSum(root.left, newSum) or self.hasPathSum(root.right, newSum)
            
        
            
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder == []:
            return None
        elif len(inorder) == 1:
            return TreeNode(inorder[0])            
        else:        
            postorder_last = postorder[len(postorder)-1]
            root_index = inorder.index(postorder_last)
            bottom_half_inorder = inorder[:root_index]
            top_half_inorder = inorder[root_index+1:]   
            bottom_half_postorder = postorder[:root_index]
            top_half_postorder = postorder[root_index:-1]              
            left = self.buildTree(bottom_half_inorder, bottom_half_postorder)
            right = self.buildTree(top_half_inorder, top_half_postorder)
            return TreeNode(postorder_last, left, right)