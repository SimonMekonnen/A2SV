# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def path (self,root,path1,p):
        cur = root
        while cur:
            path1.append(cur)
            if cur.val == p.val:
                break
            
            elif cur.val > p.val:
                cur = cur.left
            
            else:
                cur  = cur.right
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        path1 = []
        path2 = []
       
        self.path(root,path1,p)
        self.path(root,path2,q)
        
        for i in range(min(len(path1),len(path2))):
            if path1[i].val != path2[i].val:
                return path1[i - 1]
        
        return path1[i]
        
        
            
            
            
                
        