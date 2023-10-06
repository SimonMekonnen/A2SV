# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        def dfs(root,cur):
            if not root:
                return
            if not root.left and not root.right:
                cur.append(root.val)
                if sum(cur) == targetSum:
                    ans.append(cur.copy())
            
            
            
            left = dfs(root.left,cur + [root.val])
            right = dfs(root.right,cur + [root.val])
        
        dfs(root,[])
        return ans   