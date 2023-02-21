# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        right = dummy.next
        prev = dummy
        for i in range(n - 1):
            right = right.next
      
        left  = dummy.next
     
        while right and right.next:
            left = left.next
            right = right.next
            prev = prev.next
        
        prev.next = left.next
            
         
            
   
              
            
        return dummy.next
            
        
            
        