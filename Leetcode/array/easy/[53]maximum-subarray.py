# given an integer array nums find the contiguous subarray (containing
# at least one number) which has the largest sum and return its sum

#Example:
# input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# output: 6
# [4, -1, 2, 1] has largest sum = 6
def maxSubArraySum(nums, l, h):
    # base case: only one element
    if (l == h):
        return nums[l]

    # find middle point
    m = (l + h)//2

    # return maximum of the following possible cases:
    # a) max subarray sum in left half
    # b) max subarray sum in right half
    # c) max subarray sub such that the subarray crosses the midpoint
    case_a = maxSubArraySum(nums, l, m)
    case_b = maxSubArraySum(nums, m+1, h)
    case_c = maxCrossingSum(nums, l, m, h)

    return max(case_a, case_b, case_c)

def maxCrossingSum(arr, l, m, h):
    # include elements on left or mid
    sm = 0
    left_sum = -1000

    for i in range(m, l-1, -1):
        sm = sm + arr[i]
        if (sm > left_sum):
            left_sum = sm

    # include elements on right of mid
    sm = 0
    right_sum = -1000
    for i in range(m+1, h+1):
        sm = sm + arr[i]
        if (sm > right_sum):
            right_sum = sm

    # return sum of elements on left and right of mid
    # returning only left_sum + right_sum will fail for [-2,1]
    return max(left_sum + right_sum, left_sum, right_sum)

class Solution(object):
    # divide and conquer; O(NlogN)
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return maxSubArraySum(nums, 0, len(nums)-1)

    # O(N)
    def maxSubArray2(self, nums):
        total_sum = max_sum = nums[0]
        for i in nums[1:]:
            total_sum = max(i, total_sum+i)
            max_sum = max(max_sum, total_sum)
        return max_sum


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(sol.maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))
