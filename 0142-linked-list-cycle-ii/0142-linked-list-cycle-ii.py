# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow  = head
        ba = False
        while fast and fast.next:
            
            slow = slow.next
            fast  = fast.next.next
            if slow  == fast:
                ba = True
                break
        
       
        if ba  == False:
            return 
        curr = head
        
        while slow != curr:
            
            slow = slow.next
            curr = curr.next
        
        return slow
        
      
       
        
        