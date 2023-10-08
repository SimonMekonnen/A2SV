# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        def dfs(root1,root2,parent):
            if not root1 and not root2:
                return 
            if parent != -1:
                left = parent.left
                right = parent.right
            if not root1 or not root2 or root1.val != root2.val:
                c = parent.left
                parent.left = right
                parent.right=  c
            if root1.left:
                if root2 == None:
                    return
                l = dfs(root1.left,root2.left,root1)
            if root1.right:
                if root2 == None:
                    return
                r = dfs(root1.right,root2.right,root1)
        for i in range(100):
            dfs(root1,root2,-1)
        
        def dfs(root1,root2):
                if not root1 and not root2:
                    return True

                if not root1 or not root2 or root1.val != root2.val:
                    return False
                return dfs(root1.left,root2.left) and dfs(root1.right,root2.right)

        return dfs(root1,root2)
        