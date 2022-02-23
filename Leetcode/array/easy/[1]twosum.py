class Solution(object):
    # O(N^2) time
    # O(1) space
    def twoSum_bruteforce(self,nums,target):
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return -1



    # O(N) time
    # O(N) space
    def twoSum_enum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hm = dict()

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hm:
                return [hm[diff], i]
            else:
                hm[n] = i

        return -1

    # hashmap -- value : index
    # nums = [2, 1, 5, 3] , target = 4
    #         |  |  |  |
    #        4-2 = 2 doesnt exist in hashmap
    #            |  |  |
    #           4-1 = 3 doesn't exist in hashmap
    #               |  |
    #              4-5 = -1 doesn't exist in hashmap
    #                  |
    #                 4-3 = 1 exist in hashmap! (hit)
    # hashmap = [2:0, 1:1, 5:2, ]

    # enumerate(nums) returns (0, nums[0]), (1, nums[1]), ...




    # O(N) time
    # O(N) space
    def twoSum(self, nums, target):
        d = dict()
        for i in range(len(nums)):
            n1 = nums[i]
            n2 = target - n1
            if n2 in d:
                return [i,d[n2]]
            else:
                d[n1] = i
        return -1

    """
    Test Case: [2,7,11,15], 9
    ---------------------------------------
    ---------------------------------------
    i = 0 
        d = {}
        n1 = 2,     n2 = 9 - 2 = 7 
        n2 not in d --> record index of n1 in d 
        d = {2:0}
    i = 1 
        d = {2:0}
        n1 = 7      n2 = 9 - 7 = 2
        n2 in d --> return i and d[n2] (return indices of two numbers that sum up to target)
    ---------------------------------------
    result: [0,1]
    ---------------------------------------
    ---------------------------------------
    """

sol = Solution()

print(sol.twoSum_bruteforce([2,7,11,15],9))

# print(sol.twoSum([1,2,3],5))
# print(sol.twoSum([2,7,11,15],9))

# print(sol.twoSum([1,2,4],4))
