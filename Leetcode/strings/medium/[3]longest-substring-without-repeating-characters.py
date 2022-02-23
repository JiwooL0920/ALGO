class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = ""
        for i in range (len(s)): 
            substring = "" 
            for j in range(i, len(s)):
                if s[j] in substring:
                    break
                else:
                    substring += s[j] 
            if len(substring) > len(result):
                result = substring 
        return len(result) 


    def steven(self, s: str) -> int:
        def recur_subst(self, s: list, count: int, stack: list, unique_stack: list):
            
            if len(s) == 0:
                return count
            for character in s[:(len(unique_stack))]:
                if character not in stack:
                    stack.append(character)
                else:                    
                    break
            if len(stack) > count:
                count = len(stack)            
            stack.clear()
            if len(unique_stack) == count:
                return count
            return recur_subst(self, s[1:], count, stack, unique_stack)     
        str1 = s        
        str1 = list(str1)   
        stack = []
        unique_stack = []
        count = 0
        for character in str1:
            if character not in unique_stack:
                unique_stack.append(character)        
        result = recur_subst(self, str1, count, stack, unique_stack)
        return result

    def jin(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            dic = {}
            dic[s[i]] = 1
            for j in range(i+1,len(s),1):
                if s[j] in dic:
                     break
                else:
                    dic[s[j]] = 1
            if longest < len(dic):
                longest = len(dic)
        return longest