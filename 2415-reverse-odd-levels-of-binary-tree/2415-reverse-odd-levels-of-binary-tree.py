# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        
        que = deque([root])
        level = 0
        while que:
            size = len(que)
            if level % 2 == 1:
                left = 0
                right  = size - 1
                while left < right:
                    que[left].val,que[right].val = que[right].val, que[left].val
                    left += 1
                    right -= 1
                    
            for i in range(size):
                
                cur = que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            level += 1
        return root
                
        