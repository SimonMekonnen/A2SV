# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        que = deque([root])
        ans = []
        while que:
            c = len(que)
            now = []
            for i in range(c):
                cur = que.popleft()
                now.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            ans.append(now)
        
        return sum(ans[-1])
                
                
        