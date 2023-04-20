# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = dummy = ListNode()
        
        total = 0
        cur = head.next
        while cur:
            if cur.val == 0:
                dummy.next =  ListNode(total)
                dummy = dummy.next
                total = 0
            total += cur.val
            cur = cur.next
        return ans.next
        