from linkedlist import *

# construct an in-place algorithm to reverse a linked list
# naive solution:
# consider all nodes one by one then construct another linked list in reverse
# order. problem: it has O(N) memory complexity so it's not in-place
# using pointers:
# we can achieve an in-place algorithm that has O(N) linear time complexity

class Solution(LinkedList):
    def reverse(self):
        current_node = self.head
        previous_node = None
        next_node = None

        while current_node is not None:
            next_node = current_node.nextNode
            current_node.nextNode = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

if __name__ == '__main__':
    llist = Solution()
    llist.insert_end(10)
    llist.insert_end(20)
    llist.insert_end(30)

    llist.reverse()
    llist.traverse()

