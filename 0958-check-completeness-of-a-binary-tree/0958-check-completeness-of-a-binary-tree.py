# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        length = [2**i for i in range(10)]
        
        level = []
        que = deque([root])
        last = []
        while que:
            cur  = []
            b = last
            last = []
            for i in range(len(que)):
                now = que.popleft()
                cur.append(now.val)
                last.append(now.left)
                last.append(now.right)
                if now.left:
                    que.append(now.left)
                if now.right:
                    que.append(now.right)
                    
        
            level.append(cur)
    
        for i in range(len(level) - 1):
            if len(level[i]) != length[i]:
                return False
        if b:
            right = len(b) - 1
            while b[right] == None:
                right -= 1

            for i in range(right):
                if b[i] == None:
                    return False
    

        return True
        