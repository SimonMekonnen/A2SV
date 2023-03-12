# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        table = defaultdict(int)
        def helper(root):
            if not root:
                return 
            table[root.val] += 1
            helper(root.left)
            helper(root.right)
            
        helper(root)
            
        b = max(table.values())
        
        ans = []
        for i in table:
            if table[i] == b:
                ans.append(i)
        
        return ans
        