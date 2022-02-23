class Node:
	def __init__(self, name):
		self.name = name
		self.adjacency_list = []
		self.visited = False

def bfs(start_node):
	# FIFO: first item we insert will be the first one to take out
	queue = [start_node]

	# we keep iterating (consider the neighbours) until the queue becomes empty
	while queue:
		# remove and return the first item we have insert into the list
		actual_node = queue.pop()
		actual_node.visited = True
		print(actual_node.name)

		# let's consider the neighbours of the actual_node one by one
		for n in actual_node.adjacency_list:
			if not n.visited:
				queue.append(n)


if __name__ == '__main__':
	# create vertices
	node1 = Node("A")
	node2 = Node("B")
	node3 = Node("C")
	node4 = Node("D")
	node5 = Node("E")

	# handle the neighbours
	node1.adjacency_list.append(node2)
	node1.adjacency_list.append(node3)
	node2.adjacency_list.append(node4)
	node4.adjacency_list.append(node5)

	# run BFS
	bfs(node1)


