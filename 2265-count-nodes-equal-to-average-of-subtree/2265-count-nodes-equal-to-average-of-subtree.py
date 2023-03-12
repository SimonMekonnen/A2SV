# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root):
        if not root:
            return [] 
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        if (sum(left) + sum(right) + root.val) // (len(left) + len(right) + 1) == root.val:
            self.count += 1
        
        return left + [root.val] + right
        
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        self.count = 0
        
        self.helper(root)
        
        return self.count
        
    
        
        