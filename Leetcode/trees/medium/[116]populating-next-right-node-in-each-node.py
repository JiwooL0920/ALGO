"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
     
        queue = [root]

        while queue:
            nextLevel = []
            queue.append(None)
            for i in range(len(queue)-1):
                node = queue[i]
                if node:
                    node.next = queue[i+1]
                    if node.left:
                        nextLevel.append(node.left)
                    if node.right:
                        nextLevel.append(node.right)
                    
            queue = nextLevel
        return root





    def jin(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        queue = []
        if root:
            queue.append(root)
            while queue:
                q_size = len(queue)
                same_level_queue = []
                for i in range(q_size):
                    curr_node = queue[0]
                    same_level_queue.append(curr_node)
                    queue = queue[1:]
                    if curr_node.left:
                        queue.append(curr_node.left)
                    if curr_node.right:
                        queue.append(curr_node.right)
                for i in range(len(same_level_queue)-1):
                    same_level_queue[i].next = same_level_queue[i+1]
        return root





    # # only work till 2 depth
    # def helper(self, root: 'Node') -> 'Node':
    #     if root.left:            
    #         root.left.next = root.right  
    #         temp = depth
    #         if root.right.left and root.left.right:            
    #             root.left.right.next = root.right.left            
    #         self.helper(root.left)        
    #         self.helper(root.right)

    # def steven(self, root: 'Node') -> 'Node':
    #     if not root:
    #         return None
    #     self.helper(root)
    #     return root