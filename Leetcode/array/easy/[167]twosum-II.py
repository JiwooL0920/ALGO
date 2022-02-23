class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0 
        end = len(numbers)-1
        while start < end: 
            n1 = numbers[start]
            n2 = numbers[end]
            summ = n1 + n2
            if summ == target: 
                return [start+1,end+1]
            elif summ > target: 
                end -= 1 
            else:
                start += 1 
        