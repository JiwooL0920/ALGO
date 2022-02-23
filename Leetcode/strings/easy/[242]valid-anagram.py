class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {} 
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1 
    
        for c in t:
            if c in d:
                d[c] -= 1 
            else:
                return False 
                
        return all(v==0 for v in d.values())


    def jin(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
    
        for char in t:
            if char not in dic:
                return False
            else:
                dic[char] -= 1
                
        for key in dic:
            if dic[key] != 0:
                return False
        return True  



    def steven(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hsh_tbl = {}
        for letter in s:
            if letter in hsh_tbl:
                hsh_tbl[letter] += 1
            else:
                hsh_tbl[letter] = 1
        for letter in t:
            if letter in hsh_tbl:
                hsh_tbl[letter] -= 1
            else:
                return False
        for entry in hsh_tbl:
            if hsh_tbl[entry] != 0:
                return False
        return True