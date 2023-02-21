# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0 :
            return head
        
        last = head
        n = 1
        
        while last.next:
            n+=1
            last = last.next
        if k%n == 0:
            return head
        middle = head
        for i in range(n - k % n - 1):
            middle = middle.next
        
        first = middle.next
        middle.next = None
        last.next = head
        
        return first
        
        
        
        
        
        
        
        