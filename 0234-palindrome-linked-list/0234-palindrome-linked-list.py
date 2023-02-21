# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
         
        c = count // 2
        now = None
        curr = head
        while c:
            ne = curr.next
            curr.next = now
            now = curr
            curr = ne
            c-=1
            
        if count % 2 == 1:
            curr = curr.next
        
        while now:
            if now.val != curr.val:
                return False
            now = now.next
            curr = curr.next
        return True
            
        
        
            
        