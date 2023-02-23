# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        odd = ListNode()
        even = ListNode()
        
        curr = head 
        b = odd
        c = even
        count = 0
        while curr:
            now = curr.next
            curr.next = None
            if count % 2 == 0:
                b.next = curr
                b = b.next
            else:  
                c.next = curr
                c = c.next
            curr = now
            count += 1
            
        b.next = even.next
        
        return odd.next
        
        
            
            