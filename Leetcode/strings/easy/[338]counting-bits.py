class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [] 
        for num in range(n+1):
            bit = bin(num)[2:]
            occ = bit.count('1')
            result.append(occ)
        return result 
        


    def jin(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # n=2
        res = []
        for i in range(n+1):
            bin_num = bin(i)[2:]
            counter = 0
            for j in range(len(bin_num)):
                if bin_num[j]=="1":
                    counter+=1
            res.append(counter)        
          
        return res


    def steven(self, n):
        if n == 0:
            return [0]           
        return self.countBits(n-1) + [bin(n)[2:].count("1")] 