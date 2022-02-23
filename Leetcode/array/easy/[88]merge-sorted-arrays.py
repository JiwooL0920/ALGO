class Solution(object):
	def merge(self, nums1, m, nums2, n):
		"""
		:type nums1: List[int]
		:type m: int
		:type nums2: List[int]
		:type n: int
		:rtype: None Do not return anything, modify nums1 in-place instead.
		"""

		while m > 0 and n > 0:
			if nums1[m - 1] >= nums2[n - 1]:
				nums1[m + n - 1] = nums1[m - 1]
				m -= 1
			else:
				nums1[m + n - 1] = nums2[n - 1]
				n -= 1
			print(nums1)

		for i in range(0, n):
			nums1[i] = nums2[i]

		return nums1


	"""
	merge([4,5,6,0,0,0], 3, [1,2,3], 3)
	---------------------------------------
	---------------------------------------
	<< START WHILE LOOP >>
	   m = 3         n = 3
	[4,5,6,0,0,0]   [1,2,3]
		 ^               ^       
	nums1[2] = 6     >    nums2[2] = 3 
	nums1[5] = nums1[2] 
	nums1 = [4,5,6,0,0,6]
	m -= 1
	---------------------------------------
	   m = 2 	     n = 3
	[4,5,6,0,0,6]   [1,2,3]
	   ^                 ^
	nums1[1] = 5     >    nums2[2] = 3 
	nums1[4] = nums1[1] 
	nums1 = [4,5,6,0,5,6]
	m -= 1
	---------------------------------------
	   m = 1         n = 3
	[4,5,6,0,5,6]   [1,2,3]
	 ^                   ^
	 nums1[0] = 4    >    nums2[2] = 3
	 nums1[3] = nums1[0] 
	 nums1 = [4,5,6,4,5,6]
	 m -= 0
	---------------------------------------
	<< FINISH WHILE LOOP, START FOR LOOP >>
	i = 0 
		nums1[0] = nums2[0] 
		nums1 = [1,5,6,4,5,6]
	i = 1
		nums1[1] = nums2[1]
		nums1 = [1,2,6,4,5,6]
	i = 2
		nums1[2] = nums2[2]
		nums2 = [1,2,3,4,5,6]
	---------------------------------------
	---------------------------------------		
	"""



sol = Solution()
# sol.merge([1,2,3,0,0,0],3,[2,5,6],3)
sol.merge([4,5,6,0,0,0],3,[1,2,3],3)
