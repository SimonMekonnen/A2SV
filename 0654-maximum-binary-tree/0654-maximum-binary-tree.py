# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        now = []
        m = max(nums)
        def helper(arr):
            nonlocal now
            if len(arr) == 0:
                return None
            if len(arr) == 1:
                now.append(TreeNode(arr[0]))
                return TreeNode(arr[0])
            i = arr.index(max(arr))
            root = TreeNode(arr[i])
            root.left = helper(arr[:i])
            root.right = helper(arr[i + 1:])
            now.append(root)
            return root

     
        helper(nums)
        for i in now:
            if i.val == m:
                return i
     
        
                                    
                                
        