# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        stk = []
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        ans = [0] * count
        
        cur = head 
        d = 0
        while cur:
            while stk and stk[-1][0] < cur.val:
                c = stk.pop()
                ans[c[1]] = cur.val
            stk.append([cur.val,d])
            cur = cur.next
            d += 1
        
        return ans
            
        