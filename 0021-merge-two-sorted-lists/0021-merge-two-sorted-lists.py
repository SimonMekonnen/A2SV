# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        cur = None  
        while list1 and list2:
            if list1.val >= list2.val:
                cur = list2.next
                list2.next = None
                ans.append(list2)
                list2 = cur
            else:
                cur = list1.next
                list1.next = None
                ans.append(list1)
                list1 = cur
        if list1:
            ans.append(list1)
        if list2:
            ans.append(list2)
        for i in range(len(ans)-2,-1,-1):
            ans[i].next = ans[i+1]
        return ans[0] if ans else None
        
                
            
