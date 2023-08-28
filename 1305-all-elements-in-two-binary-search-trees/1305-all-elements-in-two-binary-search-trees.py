# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def travers(root):
            if not root:
                return []
            
            return [root.val] + travers(root.left) + travers(root.right)
        
        return sorted(travers(root1) + travers(root2))