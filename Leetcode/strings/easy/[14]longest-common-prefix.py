class Solution(object):    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lcp = strs[0]
        for s in strs[1:]:
            common = ""
            for i in range(min(len(s), len(lcp))): 
                c_s = s[:i+1]
                c_lcp = lcp[:i+1]
                if c_s != c_lcp:
                    break 
                else:
                    common = c_s 
            lcp = common 

        return lcp 




    def jin(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if strs is empty -> return ""
        # else
        
        # Get the length of shortest element
        shortest_len = 0
        for i in range(len(strs)):
            if i==0:
                shortest_len = len(strs[i])
            else:
                if shortest_len > len(strs[i]):
                    shortest_len = len(strs[i])
        

        counter = 1
        cmm_words = ""
        for i in range(shortest_len): # 4 times [0:1] ~ [0:5]
            for j in range(len(strs)):
                if j==0:
                    cmm_words = strs[j][0:i+1]
                else:
                    if strs[j][0:i+1] != cmm_words:
                        return cmm_words[:-1]
        return cmm_words
