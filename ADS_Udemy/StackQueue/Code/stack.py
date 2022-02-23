# LIFO: last in first out

class Stack:
    def __init__(self):
        self.stack = [] # one dimensional array

    # insert item into the stack; O(1)
    def push(self, data):
        self.stack.append(data)

    # remove and return the last item we have inserted (LIFO); O(1)
    def pop(self):
        if self.stack_size() < 1: # stack is empty
            return
        data = self.stack[-1]
        del self.stack[-1]
        return data

    # return the last item without removing it; O(1)
    def peek(self):
        return self.stack[-1]

    # O(1)
    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print('Size: %d' % stack.stack_size())
print('popped item: %d' % stack.pop())
print('Size: %d' % stack.stack_size())
print('peeked item: %d' % stack.peek())
print('Size: %d' % stack.stack_size())
