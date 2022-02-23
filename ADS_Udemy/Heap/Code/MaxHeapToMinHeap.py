"""
Transform a max heap to min heap

Solution:
We have to consider the internal nodes exclusively (in reversed order)
Leaf nodes don't have children so no need to check heap properties
In every iteration we consider an internal node. Find smallest child and swap with parent
So:
	consider internal nodes in reversed order and call fixDown()
"""
class HeapTransformer:
	def __init__(self, heap):
		self.heap = heap

	def transform(self):
		# start in reversed order, going up to the root node
		for i in range((len(self.heap)-2)//2, -1, -1):
			self.fix_down(i)

	def fix_down(self, index):
		index_left = 2 * index + 1
		index_right = 2 * index + 2

		# in a max heap the parent is always greater than the children
		index_largest = index

		# looking for the largest (parent or left node)
		if index_left < len(self.heap) and self.heap[index_left] < self.heap[index]:
			index_largest = index_left

		# if the right child is smaller than the left child: min is right child
		if index_right < len(self.heap) and self.heap[index_right] < self.heap[index_largest]:
			index_largest = index_right

		# if the parent is larger than the children: it as a valid heap so we terminate the recursive function calls
		if index != index_largest:
			self.heap[index], self.heap[index_largest] = self.heap[index_largest], self.heap[index]
			self.fix_down(index_largest) # call function recursively on node we've swapped




if __name__ == '__main__':
	n = [210, 100, 23, 2, 5]
	heap_transform = HeapTransformer(n)
	heap_transform.transform()
	print(heap_transform.heap)
