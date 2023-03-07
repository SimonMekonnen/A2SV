# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root):
            if not root:
                return []
        
            left = helper(root.left)
            right = helper(root.right)
        
            return left + [root.val] + right
        c = helper(root)
        
        for i in range(1,len(c)):
            if c[i] <= c[i - 1]:
                return False
        return True

        