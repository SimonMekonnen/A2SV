# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        dummy = ListNode(-inf)
        ans = dummy
        dummy.next = head
        cur = head
        while cur:
            start = dummy.next
            prev = dummy
            while start != cur and cur.val > start.val:
                start = start.next
                prev = prev.next  
            now = dummy.next
            nowprev = dummy
            while now and now.next and now != cur:
                now = now.next 
                nowprev = nowprev.next
            tobe = cur.next
            if cur != start:
                yeprev = prev.next
                prev.next = cur
                cur.next = yeprev
                nowprev.next = tobe
            cur = tobe
        return dummy.next
                
                
                
            
        
        