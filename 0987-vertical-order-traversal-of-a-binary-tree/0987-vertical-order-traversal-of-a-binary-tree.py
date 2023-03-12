# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root, row, col):
        
        if not root:
            return []
        
        return self.helper(root.left,row + 1,col - 1) + [[col,row,root.val]] + self.helper(root.right,row + 1, col + 1)
        
        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        inorder = self.helper(root,0,0)
        inorder.sort()
        _min = inf
        _max = -inf
        for i in inorder:
            
            _min = min(_min,i[0])
            _max = max(_max,i[0])
            
        length = _max - _min
    
        ans = [[] for i in range(length + 1)]

        for i in inorder:
            
            ans[i[0] - _min].append(i[2])
            
        return ans
        
        
            
            
            
        
            
        
        
        
        