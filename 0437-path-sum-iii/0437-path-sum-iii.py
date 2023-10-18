# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        dic = defaultdict(int)
        dic[0] = 1
        ans = 0
        def dfs(root,total):
            nonlocal ans
            if not root:
                return 
            
            ans += dic[total + root.val - targetSum]
            dic[total + root.val] += 1
            
            dfs(root.left,total + root.val)
            dfs(root.right,total + root.val)
            dic[total + root.val] -= 1
        dfs(root,0)
        return ans