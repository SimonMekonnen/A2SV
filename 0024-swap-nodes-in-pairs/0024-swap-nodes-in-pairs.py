# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        prev = ListNode()
        ans = prev
        slow = head
        fast = head.next
        
        while fast:
            after = fast.next
    
            b = slow.next.next
            if fast.next:
                c = fast.next.next
            else:
                c = None
            fast.next = slow
            slow.next = after
            prev.next = fast
            prev = slow
            slow = b
            fast = c
        
        return ans.next
            
        
            
            
        
        
        
        