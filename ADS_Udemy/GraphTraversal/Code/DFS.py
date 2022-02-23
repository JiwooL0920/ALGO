class Node:
	def __init__(self, name):
		self.name = name
		self.adjacency_list = []


def depth_first_search(start_node):
	# that we need a LIFO: last item we insert is the first one we take out
	stack = [start_node]

	# let's iterate until stack becomes empty
	while stack:
		# pop() returns last item we've inserted - O(1)
		actual_node = stack.pop()
		actual_node.visited = True
		print(actual_node.name)
		for n in actual_node.adjacency_list:
			# if the node has not been visited so far
			if not n.visited:
				# insert the item into stack
				stack.append(n)


# second implementation
# only difference is how to set the nodes to be visited
# whenever we consider the adjacent nodes (and the node is not visited), this is when we set it to be visited
# this is how we can avoid revisiting (and reinserting into the stack) the already visited nodes
def dfs(start_node):
	# that we need a LIFO: last item we insert is the first one we take out
	stack = [start_node]
	# we set the start node to be visited
	start_node.visited = True

	# let's iterate until the stack becomes empty
	while stack:
		# pop() returns last item we've inserted - O(1)
		actual_node = stack.pop()
		print(actual_node.name)

		for n in actual_node.adjacency_list:
			# if the node has not been visited so far
			if not n.visited:
				n.visited = True
				# insert item into stack
				stack.append(n)

def dfs_recursion(node):
	node.visited = True
	print(node.name)
	for n in node.adjacency_list:
		if not n.visited:
			dfs_recursion(n)


if __name__ == '__main__':
	# first we have to create the vertices (nodes)
	node1= Node("A")
	node2 = Node("B")
	node3 = Node("C")
	node4 = Node("D")
	node5 = Node("E")

	# handle and set the neighbors accordingly
	node1.adjacency_list.append(node2)
	node1.adjacency_list.append(node3)
	node2.adjacency_list.append(node4)
	node4.adjacency_list.append(node5)

	# run DFS
	depth_first_search(node1)






