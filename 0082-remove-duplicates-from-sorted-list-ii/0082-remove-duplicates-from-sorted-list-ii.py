# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(inf)
        now = dummy
        cur = head
        while cur:
            flag = False
            while cur and cur.next and cur.val == cur.next.val:
                flag = True
                cur = cur.next
            c = cur.next
            if not flag:
                cur.next = None
                now.next = cur 
                now = now.next
            cur = c
        
        return dummy.next
            
        
        
        
                
      
                
      