# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        # dummy = ListNode()
        cur = l1
        first = None
        while cur:
            n = cur.next
            cur.next = first
            first = cur
            cur = n
        cur = l2
        second = None
        while cur:
            n = cur.next
            cur.next = second
            second = cur
            cur = n
        ans = ListNode()
        t = ans
        carry = 0
        while first or second:
            if first and second:
                c = first.val + second.val + carry
                if len(str(c)) == 2:
                    carry = 1
                    c = int(str(c)[-1])
                else:
                    carry = 0
                ans.next = ListNode(c)
                ans = ans.next
                first = first.next
                second = second.next
            elif first:
                c = first.val + carry
                if len(str(c)) == 2:
                    carry = 1
                    c = int(str(c)[-1])
                else:
                    carry = 0
                ans.next = ListNode(c)
                ans = ans.next
                first = first.next
            elif second:
                c = second.val + carry
                if len(str(c)) == 2:
                    carry = 1
                    c = int(str(c)[-1])
                else:
                    carry = 0
                ans.next = ListNode(c)
                ans = ans.next
                second = second.next
        if carry:
            ans.next = ListNode(1)
        
        cur = t.next
        first = None
        while cur:
            n = cur.next
            cur.next = first
            first = cur
            cur = n
            
        return first
                
                
                
                