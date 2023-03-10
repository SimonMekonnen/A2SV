# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode],u = inf,l = -inf) -> bool:
        
        if not root:
            return True
        if root.val >= u or root.val <= l:
            return False
        
        return self.isValidBST(root.left,root.val,l) and self.isValidBST(root.right,u,root.val)
            
        
        
               

        