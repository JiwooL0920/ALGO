# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# inorder: left -> root -> right
# postorder: left -> right -> root 

# ------------------------------
# ('root', 3)
# ('inorder', [9, 3, 15, 20, 7])
# ('postorder', [9, 15, 7, 20, 3])
# ------------------------------
# ('bottom_half_inorder', [9])
# ('top_half_inorder', [15, 20, 7])
# ('bottom_half_postorder', [9])
# ('top_half_postorder', [15, 7, 20])
# ------------------------------
# ('root', 20)
# ('inorder', [15, 20, 7])
# ('postorder', [15, 7, 20])
# ------------------------------
# ('bottom_half_inorder', [15])
# ('top_half_inorder', [7])
# ('bottom_half_postorder', [15])
# ('top_half_postorder', [7])

class Solution:
    def buildTree(self, inorder, postorder):
        if inorder == []:
            return None
        elif len(inorder) == 1:
            return TreeNode(inorder[0])            
        else:        
            root = postorder[len(postorder)-1]
            root_index = inorder.index(root)
            bottom_half_inorder = inorder[:root_index]
            top_half_inorder = inorder[root_index+1:]   
            bottom_half_postorder = postorder[:root_index]
            top_half_postorder = postorder[root_index:-1]     
            left = self.buildTree(bottom_half_inorder, bottom_half_postorder)
            right = self.buildTree(top_half_inorder, top_half_postorder)
            return TreeNode(root, left, right)
        
        