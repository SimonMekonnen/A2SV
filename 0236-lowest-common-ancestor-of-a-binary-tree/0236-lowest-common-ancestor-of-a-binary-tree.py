# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        pos = None
        def dfs(root,p,q):
            nonlocal ans,pos
            if not root:
                return False
            if root.val == p or root.val == q:
                pos = root
                return True
            
            left = dfs(root.left,p,q)
            right = dfs(root.right,p,q)
            if left and right:
                ans = root
                return 
            return left or right
        dfs(root,p.val,q.val)
        return ans if ans else pos