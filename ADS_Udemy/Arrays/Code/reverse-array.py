# Reverse a T[] array in O(N) linear time complexity and we want the
# algorithm to be in-place as well - so no addition memory can be used
# ex. input = [1,2,3,4,5], output = [5,4,3,2,1]

# my solution
def reverse(arr):
    start = 0;
    end = len(arr)-1;
    while (start <= end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# solution
def reverse_sol(nums):
    # pointing to the first item
    start_index = 0
    # pointing to the last item
    end_index = len(nums)-1

    while end_index > start_index:
        # keep swapping the items
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index = start_index + 1
        end_index = end_index - 1





if __name__ == '__main__':
    # my solution
    arr = [1,2,3,4,5]
    reverse(arr)
    print(arr)

    # solution
    n = [1,2,3,4]
    reverse_sol(n)
    print(n)
