# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        val = 0
        while fast and fast.next:
            val+=1
            slow = slow.next
            fast = fast.next.next
        if val == 0 or val ==  1 and slow.next == None:
            if val == 0:
                head = None
            else:
                head.next = None
            return head
        slow.val = slow.next.val
        slow.next = slow.next.next
        return head
        