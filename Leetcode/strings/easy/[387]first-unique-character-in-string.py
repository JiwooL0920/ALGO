class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1         
        
        for c in s:
            if d[c] == 1:
                return s.index(c)
            
        return -1
            
             
            
            
            
    def steven(self, s):
        dic = {}
        lst = []
        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
            lst.append(char)
        for i in range(len(lst)):
            if dic[lst[i]] == 1:
                return i
        return -1



    def jin(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                dic[s[i]] = -1
        checker = -1
        for key in dic:
            if checker == -1 and dic[key] >= 0:
                checker = dic[key]
            elif dic[key] < checker and dic[key] >= 0:
                checker = dic[key]
        return checker  