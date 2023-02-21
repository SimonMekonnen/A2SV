# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(head,left,right):
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
        
        curr = head
        count = 0
        while curr:
            count+=1
            curr = curr.next
        if  k == count or k == 0 or count == 0 or k % count == 0:
            return head
        
        k = k % count
        
      
        return reverse(reverse(reverse(head,count - k + 1,count),1,count - k),1,count)
    
        
        
        
        
        
        
        
        