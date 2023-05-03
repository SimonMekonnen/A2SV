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
            if not root.left and not root.right:
                ar.append(str(root.val))
                arr.append(ar.copy())
                return 
            ar.append(str(root.val))
            if root.left:
                sumNumbers(root.left,ar)
                ar.pop()
            if root.right:
                sumNumbers(root.right,ar)
                ar.pop()
           
        sumNumbers(root,[])
        ans = 0
        for i in arr:
            ans += int("".join(i))

        return ans
        
        