class Solution(object):

	def bruteForce(self, nums1, nums2):
		d = dict()

		# O(N) time
		# O(N) space

		for n in nums1:
			if n in d:
				d[n] = [d[n][0] + 1, d[n][1]]
			else:
				d[n] = [1,0]

		for n in nums2:
			if n in d:
				d[n] = [d[n][0], d[n][1] + 1]
			else:
				d[n] = [0,1]

		result = []
		for n in d:
			if n in d:
				occurrence = min(d[n][0], d[n][1])
				result.extend([n] * occurrence)

		return result


	def intersect(self, nums1, nums2):
		nums1.sort()
		nums2.sort()

		# O(NlogN) time
		# O(N) space

		i = 0
		j = 0
		result = []
		while i < len(nums1) and j < len(nums2):
			n1 = nums1[i]
			n2 = nums2[j]
			if n1 < n2:
				i += 1
			elif n1 > n2:
				j += 1
			else:
				result.append(n1)
				i += 1
				j += 1

		return result




sol = Solution()
sol.intersect([4,9,5],[9,4,9,8,4])

