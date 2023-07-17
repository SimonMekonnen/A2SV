# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        cur = root
        def getright(root):
            if not root:
                return 0
            
            return getright(root.left) + root.val + getright(root.right)
        
        def dfs(root,prev):
            if not root:
                return 
            cur = getright(root.right)
            root.val += cur + prev
            dfs(root.left,root.val)
            dfs(root.right,prev)
            return root
        
        return dfs(root,0)
        
            
        