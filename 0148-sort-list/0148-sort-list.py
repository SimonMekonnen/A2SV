# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            
            return head
        
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        
        r = slow
        prev.next = None
    
        left = self.sortList(head)
        right = self.sortList(r)
        
        ans = ListNode(0)
        b = ans
            
        l = left
        r = right

        while l and r:
                
            if l.val < r.val:
                b.next = l
                l = l.next
                
            else:
                b.next = r
                r = r.next
                
            b = b.next
        if l:
            b.next = l
        if r:
            b.next = r
            
        return ans.next
        
        
        
        