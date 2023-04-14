"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        ans = 0
        if not root:
            return 0
        def helper(root,count):
            nonlocal ans
            ans = max(ans,count)
            if not root:
                return 
            for i in root.children:
                helper(i,count + 1)
        helper(root,1)
        return ans
        
    
        