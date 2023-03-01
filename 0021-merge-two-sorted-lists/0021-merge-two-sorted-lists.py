# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        Node = ListNode()
        b = Node
        def helper(l1,l2,Node):
            
            if l1 == None:
                Node.next = l2
                Node = l2
                return None
            if l2 == None: 
                Node.next = l1
                Node = l1
                return None
            
            if l1.val > l2.val:
                Node.next = l2
                Node = l2
                l2 = l2.next
            else:
                Node.next = l1
                Node = l1
                l1 = l1.next
            
            helper(l1,l2,Node)
        helper(list1,list2,Node)
        return b.next
        