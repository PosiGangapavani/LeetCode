# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        even = None 
        odd = None
        evenEnd = None 
        oddEnd = None 
        current = head 
        start = 1
        while current:
            if start % 2 == 0 and even == None:
                even = ListNode(current.val)
                evenEnd = even 
            elif start % 2 == 0:
                evenEnd.next = ListNode(current.val)
                evenEnd = evenEnd.next 
            elif start % 2 != 0 and odd == None:
                odd = ListNode(current.val)
                oddEnd = odd 
            elif start % 2 != 0:
                oddEnd.next = ListNode(current.val)
                oddEnd = oddEnd.next 
            current = current.next 
            start += 1
        oddEnd.next = even 
        return odd
        