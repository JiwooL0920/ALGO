        # if left:
        #     print("left", left.val)
        # elif not left:
        #     print("left", "none")
        # if right:
        #     print("right", right.val)
        # elif not right:
        #     print("right", "none")


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None 
        if root == p or root == q:
            return root 
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
    
        if left and right:
            return root
        if not left:
            return right 
        if not right:
            return left
                        







    def contains(self, root, n1, n2, b1=False, b2=False):
        if not root:
            return (b1, b2)
        if root == n1:
            b1 = True
        if root == n2:
            b2 = True
        (b3, b4) = self.contains(root.left, n1, n2, b1, b2)
        (b5, b6) = self.contains(root.right, n1, n2, b1, b2)
        return (b3 or b5, b4 or b6)
            
    def steven(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        (p0, q0) = self.contains(root.left, p, q)
        (p1, q1) = self.contains(root.right, p, q)
        if (p0 and q1) or (p1 and q0):
            return root
        if (root == p and (q0 or q1)) or (root == q and (p0 or p1)):
            return root
        if p0 and q0:
            return self.lowestCommonAncestor(root.left, p, q)
        if p1 and q1:
            return self.lowestCommonAncestor(root.right, p, q)
        




    def jin(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_res = []
        q_res = []
        def p_checker(root, stack):
            if root:
                stack.append(root)
                p_checker(root.left, stack)
                p_checker(root.right, stack)
                if root == p:
                    for val in stack:
                        p_res.append(val)
                stack.pop()
        def q_checker(root, stack):
            if root:
                stack.append(root)
                q_checker(root.left, stack)
                q_checker(root.right, stack)
                if root == q:
                    for val in stack:
                        q_res.append(val)
                stack.pop()                  
        p_checker(root, [])
        q_checker(root,[])
        for i in range(len(p_res)):
            for j in range(len(q_res)):
                if p_res[-1*(i+1)].val == q_res[-1*(j+1)].val:
                    return p_res[-1*(i+1)]