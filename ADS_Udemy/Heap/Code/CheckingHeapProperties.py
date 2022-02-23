"""
Check whether a list contains a valid min heap or not
Input heap is a list data structure containing integers
Hint: you just have to check the heap properties (in a min heap the parent is smaller than the children)

Solution:
We have heap and array representation
Node with index i has left child (2*i+1) and right child (2*i+2)
We just have to check these properties to verify the heap
No need to check the leaf nodes (they don't have children)
If 2*i+1 or 2*i+2 is out of range of the array then we know the node with index i is a leaf node
We just have to check the items where 2*i+2 <= N where N is the size of the array
"""

def is_min_heap(heap):
    # there is no need to check the leaf nodes
    num_items = (len(heap) - 2) // 2 # rearrange 2*i+2 <= N

    for i in range(num_items):
        # we have to check the heap property
        # parent must be smaller than the children
        if heap[i] > heap[2*i+1] or heap[i] > heap[2*i+2]:
            return False

        return True

if __name__ == '__main__':
    n = [4,6,3,2,-2]
    print(is_min_heap(n))
    n2 = [1,2,3,4,5]
    print(is_min_heap(n2))