# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(root,arr):
            if not root.left and not root.right:
                ans.append(arr + [str(root.val)])
            if root.left:
                dfs(root.left,arr + [str(root.val)] + ["->"])
            if root.right:
                dfs(root.right,arr + [str(root.val)] + ["->"])
        dfs(root,[])
        
        return ["".join(i) for i in ans]
                
                
                
        