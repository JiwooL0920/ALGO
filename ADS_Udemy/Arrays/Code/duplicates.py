# We want to find duplicates in a one-dimensional array of integers in O(N)
# running time where the integer values are smaller than the length of the
# array.
# ex. [1,2,3,1,5], then the algorithm can detect that there's a duplicate
# with value 1
# NOTE: the array cannot contain items smaller than 0 and the items with
# values greater than the size of the list. This is how we can achieve
# O(N) linear running time complexity.

# we can solve this problem in O(N) without need of extra memory using
# absolute values

def find_duplicates(nums):
    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = -nums[abs(num)]
        else:
            print('Repetition found: %s' % str(abs(num)))

if __name__ == '__main__':
    # this method cannot handle vales < 0
    n = [2,6,5,3,4,3,2]
    find_duplicates(n)
