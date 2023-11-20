# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        
        def reverse(head):
            prev = None
            cur = head
            
            while cur:
                now  = cur.next
                cur.next = prev
                prev = cur
                cur = now
            
            return prev,head
            
                
        dummy = ListNode()
        ans = dummy
        cur = head
        while cur:
            
            now = cur
            count = 1
        
            while cur.next and count < k:
                cur = cur.next
                count += 1
            
            togo = None
            if cur:
                togo = cur.next
                cur.next = None
            if count == k:
                  dummy.next,dummy =   reverse(now)
            else:
                dummy.next = now
            cur = togo
            
        return ans.next
            
            
            
            
        
        
        
        
       