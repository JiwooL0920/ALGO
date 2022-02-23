class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        minn, maxx = nums[0], nums[-1]
        summ1 = sum(nums)
        summ2 = (maxx * (maxx+1)) / 2
        cond1 = maxx == 0 and len(nums) == 1
        cond2 = minn == 0 and summ1 == summ2
        if cond1 or cond2: 
            return maxx+1
        cond3 = maxx != 0 and len(nums) == 1
        cond4 = minn != 0 and summ1 == summ2
        if cond3 or cond4:
            return minn-1
        return summ2 - summ1
        
            
    def jin(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i==0:
                if nums[i]!=0:
                    return 0
            else:
                if nums[i] != nums[i-1]+1:
                    return nums[i-1]+1
        return len(nums) 



    def steven(self, nums: List[int]) -> int:
        nums.sort()        
        for i in range(0, len(nums)-1):
            if nums[i+1] != nums[i]+1:                
                return int((nums[i+1]+nums[i])/2)
        if nums[0] == 0: return len(nums)
        return 0