# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,count):
        if not root:
            return [] 
        
        left = self.helper(root.left,count)
        right = self.helper(root.right,count)
        if (sum(left) + sum(right) + root.val) // (len(left) + len(right) + 1) == root.val:
            count[0] += 1
        
        return left + [root.val] + right
        
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        count = [0]
        
        self.helper(root,count)
        
        return count[0]
        
    
        
        