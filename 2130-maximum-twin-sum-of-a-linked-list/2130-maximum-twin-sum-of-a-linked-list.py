# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        fast = head 
        slow = head 
        
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        left = slow.next
        slow.next= None
        pre = None
        
        while head:
            
            n = head.next
            head.next = pre
            pre = head
            head = n
        
        ans =  0
        while pre:
            ans = max(pre.val + left.val , ans)
            pre = pre.next
            left = left.next
        return ans
        