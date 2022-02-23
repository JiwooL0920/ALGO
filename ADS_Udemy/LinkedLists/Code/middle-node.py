from linkedlist import *

# suppose we have a standard linked list. Construct an in-place (without
# extra memory) algorithm that is able to find the middle node

# naive solution -- linear
# iterate through the list and count how many elements there are in total
# then traverse the list again and the node with index count/2 is the middle node

# using two pointers O(N)
# first pointer: traverse one node at a time
# second pointer: traverse two nodes at a time
# when the faster pointer reaches the end then the slower pointer is pointing
# to the middle node

class Solution(LinkedList):
# O(N) linear running time complexity
    def get_middle_node(self):
        fast_pointer = self.head
        slow_pointer = self.head

        # is not None
        while fast_pointer.nextNode and fast_pointer.nextNode.nextNode:
            fast_pointer = fast_pointer.nextNode.nextNode
            slow_pointer = slow_pointer.nextNode

        return slow_pointer

if __name__ == '__main__':
    llist = Solution()
    llist.insert_end(10)
    llist.insert_end(20)
    llist.insert_end(30)

    print(llist.get_middle_node().data)
