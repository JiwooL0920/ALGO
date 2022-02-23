# gien an array nums and a value val, remove all instances of that value in place and
# return the new length. Do not allocate extra space for another array, you must do this
# by modifying the input array in place with O(1) extra memory

# Example
# input = [3,2,2,3], val = 3
# output = 2, nums = [2,2]

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in range (len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

# when nums[j] equals the given value, skip this element by incrementing j
# as long as nums[j] != val, we copy nums[j] to nums[i] and increment both
# indices at the same time. Repeat this process until j reches the end of the
# array and the new length is i

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeElement([3,2,2,3],3))
