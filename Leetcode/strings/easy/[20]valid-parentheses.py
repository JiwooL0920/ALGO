class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s: 
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False 
                prev = stack.pop()
                if c == ')' and prev != '(':
                    return False 
                if c == ']' and prev != '[':
                    return False 
                if c == '}' and prev != '{':
                    return False 
        return len(stack) == 0
            