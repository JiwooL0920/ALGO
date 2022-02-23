# given a sorted array of distinct integer and a target value,
# return the index if the target is found. if not, return the
# index where it would be if it were inserted in order

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start + end)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid-1
            else:
                start = mid+1
        return start

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1,3,5,6],2))
    """
    [1, 3, 5, 6]
    start = 0
    end = 3
    mid = 1
    2 < 3 (case 2)

    start = 0
    end = 0
    mid = 0
    3 > 1 (case 3)

    start = 1
    end = 0 ---> out of while loop

    return 1
    """
    # print(sol.searchInsert([1,2,6,6,6,7,8],6))
