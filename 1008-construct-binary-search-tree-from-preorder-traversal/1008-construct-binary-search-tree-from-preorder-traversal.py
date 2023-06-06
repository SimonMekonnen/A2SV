# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(arr):
           
            if len(arr) == 1:
                return TreeNode(arr[0])
            if not arr:
                return None
            
            now = TreeNode(arr[0])
            greater = len(arr)
            less = len(arr)
            for i in range(1,len(arr)):
                if arr[i] > arr[0]:
                    greater = i
                    break
            for i in range(1,len(arr)):
                if arr[i] < arr[0]:
                    less = i
                    break
            now.left = helper(arr[less:greater])
            now.right = helper(arr[greater : ])
            return now
        return (helper(nums))
        
            
                
                
            
        