# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        ans = []
        arr = defaultdict(int)
        def dfs(root):
            if not root:
                return "#" 
            s = str(root.val) + "," + dfs(root.left) + "," + dfs(root.right)
            if arr[s] == 1:
                ans.append(root)
            arr[s] += 1
            return s
        dfs(root) 
        return ans