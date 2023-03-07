# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            cur = root
            if not root:
                return TreeNode(val)
            while cur:
                prev = cur
                if cur.val > val:
                    cur = cur.left
                elif cur.val < val:
                    cur = cur.right

            if prev.val < val:
                prev.right = TreeNode(val)
            else:
                prev.left = TreeNode(val)

            return root
        
        
        