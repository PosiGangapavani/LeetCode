# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        dummy = headA 
        dummy1 = headB 
        while dummy != dummy1:
            if dummy == None:
                dummy = headB 
            else:
                dummy = dummy.next 
            if dummy1 == None:
                dummy1 = headA 
            else:
                dummy1 = dummy1.next 
        return dummy
        