import math 

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {} 
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        
        majority = 0 
        elem = None 
        for n in d:
            if d[n] > majority:
                majority = d[n] 
                elem = n
        
        return elem 
        

    def jin(self, nums):
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        checker = [0,0]
        for key in dic:
            if dic[key] > checker[0]:
                checker[0] = dic[key]
                checker[1] = key
        return checker[1]        
        


    def steven(self, nums):
        dict_el = {}
        length = math.floor(len(nums)/2)
        for elem in nums:
            if elem in dict_el:
                dict_el[elem] += 1
            else:
                dict_el[elem] = 1
        for key, value in dict_el.items():
            if value > length:
                return key
        return []
        
