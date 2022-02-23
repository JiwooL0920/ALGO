# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		prev = None
		curr = head
		while curr:
			nextNode = curr.next
			curr.next = prev
			prev = curr
			curr = nextNode
		return prev

	'''
	1 -> 2 -> 3 -> 4 -> 5
	^
		nextNode = curr.next = 2
		curr.next = prev = None 
		prev = curr = 1 
		curr = nextNode = 2 

	(<-) 1 -> 2 -> 3 -> 4 -> 5
			  ^
		nextNode = curr.next 3
		curr.next = prev = 1 
		prev = curr = 2 
		curr = nextNode = 3 

	1 <- 2 -> 3 -> 4 -> 5
			  ^
		nextNode = curr.next = 4
		curr.next = prev = 2 
		prev = curr = 3 
		curr = nextNode = 4

	1 <- 2 <- 3 -> 4 -> 5
				   ^
		nextNode = curr.next = 5
		curr.next = prev = 3
		prev = curr = 4
		curr = nextNode = 5

	1 <- 2 <- 3 <- 4 -> 5
						^
		nextNode = curr.next = None 
		curr.next = prev = 4
		prev = curr = 5
		curr = nextNode = None 

	1 <- 2 <- 3 <- 4 <- 5
						   ^
		curr = None
		break while loop 

	return prev --> node 5 


	'''

	def jin(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		# Empty case
		if head == None:
			return None
		# One element case
		if head.next == None:
			return ListNode(head.val, None)
		# Else
		tmp = None
		while (head != None):
			if tmp == None:
				tmp = ListNode(head.val, None)
			else:
				builder = ListNode(head.val, tmp)
				tmp = builder
			head = head.next
		return builder
