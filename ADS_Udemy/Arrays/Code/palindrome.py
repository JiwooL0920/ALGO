# design an optimal algorithm for checking whether a given string is a
# palindrome or not

# my solution
def palindrome(arr):
    start = 0
    end = len(arr)-1
    while (start < end):
        if (arr[start] != arr[end]):
            return False
        start += 1
        end -= 1
    return True

# solution
def palindrome_python(s):
    if s == s[::-1]: # if reversing string is same
        return True
    return False

# from previous question; O(N)
def reverse_sol(nums):
    # string into a list of characters
    nums = list(nums)

    # pointing to the first item
    start_index = 0
    # pointing to the last item
    end_index = len(nums)-1

    while end_index > start_index:
        # keep swapping the items
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index = start_index + 1
        end_index = end_index - 1

    # transform the list of letters into a string
    return ''.join(nums)

# it has O(s) so basically linear running time complexity as far as the number
# of letters in the strings is concerned
def is_palindrome(s):
    original_string = s
    # this is what we implemented in previous lecture in O(N)
    reversed_string = reverse_sol(s)
    if original_string == reversed_string:
        return True
    return False

if __name__ == '__main__':
    # my solution
    arr = ['r','a','c','e','c','a','r']
    arr2 = ['h','e','l','l','o']
    print(palindrome(arr))
    print(palindrome(arr2))

    # solution
    print(palindrome_python('madam'))

    print(is_palindrome('madam'))
