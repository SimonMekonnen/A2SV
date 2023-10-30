# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        to_delete = set(to_delete)
        ans = []
        
        def dfs(root):
            if not root:
                return None
            
            
            left = dfs(root.left)
            right = dfs(root.right)
     
            if root.val in to_delete:
                if left:
                    ans.append(left)
                if right:
                    ans.append(right)
                return None
            
            root.left = left
            root.right = right
            
            return root
        if dfs(root):
            ans.append(root)
        return ans
        
            
            