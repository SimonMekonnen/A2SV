# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        arr = []
        def sumNumbers(root,ar):
            nonlocal arr
            if not root:
                return 
            ar.append(str(root.val))
            sumNumbers(root.left,ar)
            sumNumbers(root.right,ar)
            if not root.left and not root.right:
                arr.append(ar.copy())
            ar.pop()
            
        sumNumbers(root,[])
        ans = 0
        for i in arr:
            ans += int("".join(i))
        return ans
        
        