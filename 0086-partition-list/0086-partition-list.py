# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        great =ListNode()
        
        dummy = great
        dummy2 = less
        current = head
        while current:
            
            hey  = current.next
            if current.val >= x:
                current.next = None
                great.next = current
                great = current
            
            else:
                current.next = None
                less.next = current
                less = current
            current = hey
        
        cur = dummy2
        while cur.next:
            cur = cur.next
        
        cur.next = dummy.next
        
        return dummy2.next
        
    
            
                
        
        
                
                
        
        