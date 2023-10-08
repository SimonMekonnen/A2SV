# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val == root.val or q.val == root.val:
            return root
        ans = None
        def dfs(root,p,q):
            nonlocal ans
            if not root:
                return False
            if root.val == p or root.val == q:
                return True
            
            left = dfs(root.left,p,q)
            right = dfs(root.right,p,q)
            if left and right:
                ans = root
                return 
            return left or right
        dfs(root,p.val,q.val)
        
        if not ans:
            def dfs(root,p,q):
                if not root:
                    return 
                if root.val == p.val:
                    return root
                if root.val == q.val:
                    return root
                left = dfs(root.left,p,q)
                right = dfs(root.right,p,q)
                if left != None:
                    return left
                if right != None:
                    return right
        
            return dfs(root,p,q)
     
        return ans