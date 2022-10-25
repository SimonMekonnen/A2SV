# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        cur = dummy = ListNode()
        while l1 or l2:
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0
            s = l1v + l2v + c
            cur.next = ListNode(val = s % 10)
            cur = cur.next
            c = 1 if s > 9 else 0
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if c == 1:
            cur.next = ListNode(val = 1)  
        return dummy.next
       