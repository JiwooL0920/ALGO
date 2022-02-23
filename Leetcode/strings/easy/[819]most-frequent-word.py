class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        specialChar = "!?',;."
        for c in specialChar:
            if c in paragraph:
                paragraph = paragraph.replace(c, " ")
            
        d = {}
        for s in paragraph.split(" "):
            s = s.lower()
            if s in d:
                d[s] += 1 
            else:
                d[s] = 1
                    
        maxCount = 0 
        mostFrequentWord = "" 
        for k in d: 
            if k not in banned and d[k] > maxCount and k!="":
                maxCount = d[k]
                mostFrequentWord = k 
                
        return mostFrequentWord 





    def jin(self, paragraph: str, banned: List[str]) -> str:
        dic = {}
        checker = ""
        for i in range(len(paragraph)):
            if paragraph[i].isalpha():
                checker += paragraph[i]
            else:
                if checker !="":
                    if checker.lower() in dic:
                        dic[checker.lower()] += 1
                    else:
                        dic[checker.lower()] = 1
                    checker = ""
        if checker !="":
            dic[checker.lower()] = 1     
        counter = 0
        saver = ""
        for word in dic:
            if dic[word] > counter and word not in banned:
                counter = dic[word]
                saver = word
        return saver   