class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    # this is why we like linked list; O(1)
    def insert_start(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)
        # check if linkedlist is empty
        if not self.head:
            self.head = new_node
        # there already is a head node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    # O(N)
    def insert_end(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)
        # if linkedlist is empty
        if not self.head:
            self.head = new_node
            return
        # point to first node of linkedlist
        actual_node = self.head
        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode
        # at the end now
        actual_node.nextNode = new_node

    # O(1)
    def size_of_linkedlist(self):
        return self.numOfNodes

    # print; O(N)
    def traverse(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode

    # beginning O(1), arbitrary O(N)
    def remove(self, data):
        if self.head is None:
            return
        # pointers
        actual_node = self.head
        previous_node = None
        # traverse and search for node with the data
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.nextNode
        # search miss - the item is not present in the linkedlist
        if actual_node is None:
            return
        # decrement size
        self.numOfNodes -= 1
        # head node is the one we want to get rid of
        if previous_node is None:
            self.head = actual_node.nextNode
        # target is internal node
        else:
            previous_node.nextNode = actual_node.nextNode


# linked_list = LinkedList()
# linked_list.insert_start(4)
# linked_list.insert_start(3)
# linked_list.insert_start(7)
# linked_list.insert_end(10)
# linked_list.insert_end(100)
# linked_list.insert_end(1000)

# linked_list.traverse()

# print()

# linked_list.remove(3000)
# linked_list.remove(100)

# linked_list.traverse()

# print('size: %d' % linked_list.size_of_linkedlist())
