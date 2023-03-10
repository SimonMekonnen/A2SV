# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getmin(self,root):
        cur = root
        while cur and cur.right:
            cur = cur.right
        
        return cur
       
    
    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return None

        if root.val > val:
            
            root.left = self.deleteNode(root.left,val)
            
        elif root.val < val:
            
            root.right = self.deleteNode(root.right,val)
        
        else:
            
            if not root.left: 
                return root.right
            
            elif not root.right:
                return root.left
            
            c = self.getmin(root.left)
            root.val = c.val
            root.left = self.deleteNode(root.left,c.val)
            
            
            
        
        return root 
  

        