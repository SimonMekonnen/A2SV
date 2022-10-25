# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        cur = dummy = ListNode()
        while l1 and l2:
            s = l1.val + l2.val + c
            if s > 9:
                c = 1
            else:
                c = 0
            cur.next = ListNode(val = s%10)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            s = l1.val + c
            if s > 9:
                c = 1
            else:
                c = 0
            cur.next = ListNode(val = s%10)
            cur = cur.next
            l1 = l1.next
        while l2:
            s = l2.val + c
            if s > 9:
                c = 1
            else:
                c = 0
            cur.next = ListNode(val = s%10)
            cur = cur.next
            l2 = l2.next
        if c == 1:
            cur.next = ListNode(val = 1)  
        return dummy.next
       