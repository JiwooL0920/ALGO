class Solution(object):

    def jin(self, headA, headB):
        listA = set()
        currA = headA
        while currA != None:
            listA.add(currA)
            currA = currA.next
        currB = headB
        while currB != None:
            if currB in listA:
                return currB
            currB = currB.next  

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        lenA = length(headA)
        lenB = length(headB)
        
        diff = abs(lenA - lenB)
        
        longer = None 
        if lenA > lenB:
            while diff > 0: 
                headA = headA.next
                diff -= 1
        else:
            while diff > 0:
                headB = headB.next
                diff -= 1
                
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA

def length(head):
    curr = head
    count = 0
    while curr:
        curr = curr.next
        count += 1
    return count 