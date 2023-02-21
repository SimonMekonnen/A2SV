# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        
        curr = dummy
        l = 0
        while l < left - 1:
            
            curr = curr.next
            l += 1
        first = curr
        torev = curr.next
        r = 0
        curr = dummy
        while r < right + 1 :
            
            curr =  curr.next
            r+=1
        
        last = curr
        
        while torev != curr:
            b = torev.next
            torev.next = last
            last = torev
            torev = b
       
        first.next = last
        
        return dummy.next
        
       
        
        
        
            
        
            
         
        
        
        
            
      
        
            
        