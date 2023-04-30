# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if not root:
                return []
            return helper(root.left) + [root.val] + helper(root.right)
        preorder = helper(root)        
        preorder.sort()
        def build(nums):
            if len(nums) == 0:
                return
            if len(nums) == 1:
                return TreeNode(nums[0])
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = build(nums[:mid])
            root.right = build(nums[mid+1:])
            
            return root
        return build(preorder)
            