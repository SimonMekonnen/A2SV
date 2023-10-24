# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return 
        arr = []
        que = deque([root])
        
        while que:
            size = len(que)
            ans = -inf
            
            for i in range(size):
                cur = que.popleft()
                ans = max(cur.val,ans)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                
                
            arr.append(ans)
        return arr
            
        