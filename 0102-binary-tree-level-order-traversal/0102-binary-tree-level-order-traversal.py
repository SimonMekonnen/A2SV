# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root,row):
        if not root:
            return []
        
        return self.helper(root.left,row + 1) + [[root.val,row]] + self.helper(root.right, row + 1)
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        
        inorder = self.helper(root,0)
        
        length = max(inorder,key = lambda x : x[1])[1]
        
        ans = [[] for i in range(length + 1)]
        
        for i in inorder:
            
            ans[i[1]].append(i[0])
        
        return ans
        
        
        
     
        
        