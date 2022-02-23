# given a sorted array nums, remove the duplicates in place such that each element
# appears only once and returns the new length. Do not allocate extra space for
# another array, you must do this by modifying the input array in-place with O(1)
# extra memory

# Examples
# input: [1,1,2]
# output: 2, nums = [1,2]

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(N) time
        # O(1) space

        # hint: 2 pointer approach, bypass duplicates
        # i = slow pointer, j = fast pointer
        if nums == []:
            return 0

        i = 0
        for j in range(i+1, len(nums)):
            n1 = nums[i]
            n2 = nums[j]
            if n2 > n1 :
                nums[i+1], nums[j] = nums[j], nums[i+1]
                i += 1

        return i+1 # nums[:i+1] is the resulting array


    """
    Test Case: [0,0,1,1,1,2,2,3,3,4]
    -----------------------------------------------
    -----------------------------------------------
    i = 0, j = 1
        [0,0,1,1,1,2,2,3,3,4]
         ^ ^
         0 = 0. bypass
         j += 1 
    i = 0, j = 2
         [0,0,1,1,1,2,2,3,3,4]
          ^   ^
          0 < 1. so exchange nums[0+1] and nums[2]
         [0,1,0,1,1,2,2,3,3,4]
          i += 1, j += 1 
    i = 1, j = 3 
        [0,1,0,1,1,2,2,3,3,4]
           ^   ^
           1 = 1. bypass
           j += 1 
    i = 1, j = 4
        [0,1,0,1,1,2,2,3,3,4]
           ^     ^
           1 = 1. bypass
           j += 1
    i = 1, j = 5
        [0,1,0,1,1,2,2,3,3,4]
           ^       ^
           1 < 2. exchange nums[1+1] and nums[5] 
           [0,1,2,1,1,0,2,3,3,4]
           i += 1, j += 1 
    i = 2, j = 6 
        [0,1,2,1,1,0,2,3,3,4]
             ^       ^
             2 = 2. bypass
             j += 1
    i = 2, j = 7
        [0,1,2,1,1,0,2,3,3,4]
             ^         ^
             2 < 3. exchange nums[2+1] and nums[7]
             [0,1,2,3,1,0,2,1,3,4]
             i += 1, j += 1
    i = 3, j = 8
        [0,1,2,3,1,0,2,1,3,4]
               ^         ^
               3 = 3. bypass
               j += 1
    i = 3, j = 9
        [0,1,2,3,1,0,2,1,3,4]
               ^           ^
               3 < 4. exchange nums[3+1] and nums[9]
               [0,1,2,3,4,0,2,1,3,1]
    -----------------------------------------------
    << END OF FOR LOOP >>
    result: nums[:i+1] = [0,1,2,3,4] 
    return: i+1 = 4 --> 4 unique elements 
    -----------------------------------------------
    -----------------------------------------------
    """




    def steven(self, nums):
        if nums == []: return 0
        if len(nums) == 1: return 1
        i = 0
        j = 1
        while j < len(nums):
            try:
                prev = nums[i]
                curr = nums[j]
            except IndexError:
                return len(nums)
            if prev == curr:
                nums[i:j + 1] = [nums[j]]
            else:
                i += 1
                j += 1
        return len(nums)

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(sol.removeDuplicates([]))

