class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # inserts item at the end of the linked list so we have to manipulate
    # the tail node in O(1) running time
    def insert(self, data):
        new_node = Node(data)
        # linkedlist is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # there is at least 1 item in the data structure so we keep inserting
        # items at the end of the linked list
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # we can traverse a doubly linked lists in both directions
    def traverse_forward(self):
        actual_node = self.head
        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next

    def traverse_backward(self):
        actual_node = self.tail
        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.previous

if __name__ == '__main__':
    llist = DoublyLinkedList()
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)

    # 1 2 3
    llist.traverse_forward()
    # 3 2 1
    llist.traverse_backward()

