# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

# O(N) time
# O(1) space

class Solution(object):
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""
		carry = 1

		for i in range(len(digits) - 1, -1, -1): # O(N)
			if carry != 0:
				digits[i] += 1
				if digits[i] == 10:
					digits[i] = 0
					carry = 1
				else:
					carry = 0


		if digits[0] == 0:
			digits.insert(0,1) # O(N)

		return digits


	"""
	Test Case: [9,9,9]
	----------------------------------
	i = 2
		carry = 1 
		add 1 to digits[2] --> 10 
		10 = 10 --> digits[2] = 0, carry = 1
	i = 1
		carry = 1
		add 1 to digits[1] --> 10
		10 = 10 --> digits[1] = 0, carry = 1
	i = 0 
		carry = 1
		add 1 to digits[0] --> 10 
		10 = 10 --> digits[0] = 0, carry = 1
	----------------------------------
	digits[0] = 0 --> insert 1 in the beginning of digits
	----------------------------------
	output: [1,0,0,0]
	"""


	def jin(self, digits):
			"""
			:type digits: List[int]
			:rtype: List[int]
			"""
			length = len(digits)
			sum = 0
			for i in range(length):
				sum = sum + digits[-(i+1)]*10**i
			sum += 1
			str_sum = str(sum)
			list_sum = []
			for digit in str_sum:
				list_sum.append(int(digit))
			return list_sum



	def steven(self, digits):
		allNines = True
		for num in digits:
			if num != 9:
				allNines = False
				break
		length = len(digits)
		if allNines:
			return [1] + [0] * length
		carry = 1

		for i in range(length):
			if digits[length - 1 - i] == 9 and carry == 1:
				digits[length - 1 - i] = 0
			elif carry == 1:
				digits[length - 1 - i] = digits[length - 1 - i] + 1
				carry = 0
		return digits




sol = Solution()
sol.plusOne([9,9,9])