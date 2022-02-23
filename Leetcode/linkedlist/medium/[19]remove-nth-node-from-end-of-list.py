# Definition for singly-linked list.
class ListNode(object):
    def __init__(self,val, next=None):
        self.val = val
        self.next = next


	def insert(self, n):
		curr = self
		while curr.next:
			curr = curr.next
		curr.next = ListNode(n)


	def show(self):
		curr = self
		while curr:
			print(curr.data, "->", end=" ")
			curr = curr.next

class Solution(object):
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		fast = head
		slow = head

		while n > 0:
			fast = fast.next
			n -= 1

		while fast is not None:
			fast = fast.next
			slow = slow.next

		slow.next = slow.next.next


sol = Solution()
llist = ListNode(1)
llist.insert(2)

sol.removeNthFromEnd(llist, 2)