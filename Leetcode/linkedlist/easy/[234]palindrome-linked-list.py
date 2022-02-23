def isPalindrome(self, head):
	"""
	:type head: ListNode
	:rtype: bool
	"""

	prev = None
	curr = head


	rev = ListNode(curr.val)
	while curr and curr.next:
		nextNode = curr.next
		curr.next = prev
		rev.next = prev
		rev = ListNode(nextNode.val)
		prev = curr
		curr = nextNode

	print(rev)
	print(head)

	while head:
		if rev.val != head.val:
			return False
		rev = rev.next
		head = head.next

	return True

