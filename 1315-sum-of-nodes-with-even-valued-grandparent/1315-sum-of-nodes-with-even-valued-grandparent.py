# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = [0]
        def dfs(parent,gp,root):
            if not root:
                return 
            
            if gp % 2 == 0:
                ans[0] += root.val
            
            dfs(root.val,parent,root.left)
            dfs(root.val,parent,root.right)
        
        dfs(7,7,root)
        return ans[0]
       
        
        