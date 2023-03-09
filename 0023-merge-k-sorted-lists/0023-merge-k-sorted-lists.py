# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return 
        
        def helper(left,right):
            
            mid = (left + right) // 2
            
            if left == right:
                return lists[left]
            
            left  = helper(left,mid)
            right = helper(mid + 1,right)
            
            ans = ListNode(0)
            b = ans
            
            l = left
            r = right

            while l and r:
                
                if l.val < r.val:
                    b.next = l
                    l = l.next
                
                else:
                    b.next = r
                    r = r.next
                
                b = b.next
            if l:
                b.next = l
            if r:
                b.next = r
            return ans.next
        return helper(0,len(lists) - 1)
        
        
        