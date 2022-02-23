class Solution(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: None Do not return anything, modify nums in-place instead.
		"""

		# O(N) time
		# O(1) space

		i = 0
		j = 1
		while j < len(nums):
			if nums[i] != 0:
				i += 1
			if nums[i] == 0 and nums[j] != 0:
				nums[i], nums[j] = nums[j], nums[i]
				i += 1
			j += 1

		return nums


	"""
	Test Case: [0,1,0,3,12]
	-------------------------------
	i = 0, j = 1
		[0,1,0,3,12]
		 ^ ^
		nums[i] = 0, nums[i] != 0 --> switch
		[1,0,0,3,12]
		i += 1, j += 1
	i = 1, j = 2
		[1,0,0,3,12]
		   ^ ^
		nums[i] = 0, nums[j] = 0 
		j += 1
	i = 1, j = 2
		[1,0,0,3,12]
		   ^   ^
		nums[i] = 0, nums[j] != 0 --> switch
		[1,3,0,0,12]
		i += 1, j += 1
	i = 2, j = 3
		[1,3,0,0,12]
			 ^ ^
		nums[i] = 0, nums[j] = 0 
		j += 1
	i = 2, j = 4
		[1,3,0,0,12]
			 ^    ^
		nums[i] = 0, nums[j] != 0 --> switch 
		[1,3,12,0,0]
		i += 1, j += 1 
	i = 2, j = 5
		j = len(nums) --> break while loop
	-------------------------------
	output: [1,3,12,0,0]
	"""




	def jin(self, nums):
			"""
			:type nums: List[int]
			:rtype: None Do not return anything, modify nums in-place instead.
			"""
			# [0,1,0,3,12]
			index = 0
			length = len(nums)
			# [1, 3, 12, 3, 12]
			for i in range(length):
				if(nums[i]!=0):
					nums[index] = nums[i]
					index+=1
			# [1, 3, 12, 0, 0]
			for i in range(length-index):
				nums[-1*(i+1)] = 0
			return nums

sol = Solution()
sol.moveZeroes([0,1,0,3,12])
sol.moveZeroes([0,0])
sol.moveZeroes([2,0,1])
sol.moveZeroes([1,2,3,1])


# [0, 1, 0, 3, 12]
# [1, 3, 12, 0, 0]