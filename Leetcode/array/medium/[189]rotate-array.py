class Solution(object):

	def rotate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
		n = len(nums)
		k %= n
		nums[:] = nums[n - k:] + nums[:n - k]
		return nums

	"""
	Test Case 1: nums = [1,2,3,4,5,6,7], k = 3
	--------------------------------------------------
	n = 7, k = 3 % 7 = 3   so diff = 4 --> index at which to slice array 
	nums[4:] index 4 to the end --> [5,6,7]
	nums[:4] from beginning, up to right before index 4 --> [1,2,3,4]
	nums = [5,6,7,1,2,3,4]
	
	
	Test Case 2: nums = [1,2], k = 5
	--------------------------------------------------
	n = 2, k = 5 % 2 = 1 
	nums[1:] --> [2]
	nums[:1] --> [1] 
	nums = [2,1] 
	"""



	def steven(self,nums,k):
		length = len(nums)
		new_arr = [0] * length
		for i in range(length):
			new_arr[(k + i) % length] = nums[i]
		for i in range(length):
			nums[i] = new_arr[i]
		return nums

	"""
	nums = [1,2,3,4,5,6,7], k = 3
	temp = [0,0,0,0,0,0,0]
	i = 0 
		(3 % 7 = 3)
		temp[3] = nums[0]
		[0,0,0,1,0,0,0]
	i = 1
		(4 % 7 = 4)
		temp[4] = nums[1]
		[0,0,0,1,2,0,0]
	i = 2
		(5 % 7 = 5)
		temp[5] = nums[2]
		[0,0,0,1,2,3,0]
	i = 3 
		(6 % 7 = 6)
		temp[6] = nums[3]
		[0,0,0,1,2,3,4]
	i = 4 
		(7 % 7 = 0)
		temp[0] = temp[4]
		[5,0,0,1,2,3,4]
	i = 5
		(8 % 7 = 1)
		temp[1] = temp[5]
		[5,6,0,1,2,3,4]
	i = 6
		(9 % 7 = 2)
		temp[2] = temp[6]
		[5,6,7,1,2,3,4]
	"""


	def jin(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
		# Time complexity: O(n)
		# Space complexity: O(n)

		length = len(nums)
		n = k % length
		if not (length <= 1 or n == 0):
			back_l = nums[length - n:]  # length : k
			front_l = nums[0:length - n]  # length: 7-k
			for i in range(n):
				nums[i] = back_l[i]
			for j in range(n, length):
				nums[j] = front_l[j - n]



s = Solution()
# s.rotate([1,2,3,4,5,6,7],3)
s.rotate([1,2],5)