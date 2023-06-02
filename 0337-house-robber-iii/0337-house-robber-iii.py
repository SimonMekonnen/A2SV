# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dp(root,took):
            if not root:
                return 0
            
            if took == 0:
                return max(
                    root.val + dp(root.left,1) + dp(root.right,1),
                    dp(root.left,0) + dp(root.right , 0)
                          )
            if took == 1:
                return dp(root.left,0) + dp(root.right,0)
            
        return dp(root,0)

        