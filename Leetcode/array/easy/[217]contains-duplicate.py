class Solution(object):
	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		# O(N) time
		# O(1) space
		nums.sort()
		for i in range(1, len(nums)):
			if nums[i] == nums[i-1]:
				return True
		return False


	def jin(self, nums):
		dict = {}
		for i in range(len(nums)):
			if nums[i] in dict.keys():
				dict[nums[i]] += 1
			else:
				dict[nums[i]] = 1
		for i in dict.values():
			if i != 1:
				print("true")
				return True
		print("false")
		return False

sol = Solution()
sol.containsDuplicate([1,2,3,1])
sol.jin([1,2,3,1])
