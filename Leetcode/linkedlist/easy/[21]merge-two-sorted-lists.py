# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""

		# O(N) time
		# O(1) space

		head = ListNode()
		curr = head

		while l1 and l2:
			if l1.val <= l2.val:
				curr.next = l1
				l1 = l1.next
			else:
				curr.next = l2
				l2 = l2.next
			curr = curr.next

		if l1:
			curr.next = l1
		elif l2:
			curr.next = l2

		return head.next



	def jin(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""

		list1 = []
		list2 = []
		while (l1 != None):
			list1.append(l1.val)
			l1 = l1.next
		while (l2 != None):
			list2.append(l2.val)
			l2 = l2.next

		list = list1 + list2
		list.sort()

		head = ListNode()
		curr = head

		for n in list:
			curr.next = ListNode(n)
			curr = curr.next

		return head.next



	def steven(self, l1: ListNode, l2: ListNode) -> ListNode:

		# Check for empty list
		if l1 == None and l2 == None:
			return None
		if l1 == None:
			return l2
		if l2 == None:
			return l1

		# Select the starting node
		if l1.val <= l2.val:
			start = l1
		else:
			start = l2

		head = start

		if head == l1:
			l1 = l1.next
		else:
			l2 = l2.next

		while l1 != None and l2 != None:
			if l1.val <= l2.val:
				head.next = l1
				head = head.next
				l1 = l1.next
			else:
				head.next = l2
				head = head.next
				l2 = l2.next
		if l1 != None:
			head.next = l1
		if l2 != None:
			head.next = l2
		return start