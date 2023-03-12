# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        que = deque([root])
        ans = []
        if not root:
            return 
        
        while que:
            
            for i in range(len(que)):
                
                cur = que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            
            ans.append(cur.val)
        
        return ans
                
                
            
            
            
        
        
        