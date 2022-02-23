# design an efficient algorithm to reverse a given integer.
# ex. input = 1234, output = 4321

# my solution; O(N)
def int_rev(n):
    result = 0
    while n > 0:
        result *= 10
        q, r = divmod(n,10)
        result += r
        n = q
    return result

def reverse_integer(n):
    reversed = 0
    remainder = 0
    while n > 0:
        remainder = n%10
        reversed = reversed*10 + remainder
        n = n//10
    return reversed

if __name__ == '__main__':
    n = 1234
    n2 = int_rev(n)
    print(n2)

    n3 = reverse_integer(n)
    print(n3)
