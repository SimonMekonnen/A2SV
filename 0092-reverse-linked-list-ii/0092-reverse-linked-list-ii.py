# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        last = None
        l = 0
        r = 0
        while r  < right:
            if l == left - 1:
                first = cur
            if l != left:
                cur = cur.next
                l += 1
            if l == left:
                if last == None:
                    hey  = cur
                b = cur.next
                cur.next = last
                last = cur
                cur = b
             
            r += 1
   
        first.next = last
        hey.next = cur
        return dummy.next
                
                
                
                
                
        
                
                
                
                
                
                
                
        
        
        
        
       
        
        
        
            
        
            
         
        
        
        
            
      
        
            
        