# design an algorithm that can return the maximum item of a stack in O(1)
# running time complexity. We can use O(N) extra memory
# hint: we can use another stack to track the max item

from stack import *

class MaxStack(Stack):

    def __init__(self):
        self.main_stack = []
        self.max_stack = []

