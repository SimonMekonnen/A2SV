# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        cur = head
        while cur:
            cur = cur.next
            l+=1
        dummy = head
        if l == 1:
            return None
        l = l - n - 1
        if l < 0:
            return head.next
        while l  > 0:
            head = head.next
            print(head)
            l-=1
        head.next = head.next.next
        return dummy 
            
        
            
        