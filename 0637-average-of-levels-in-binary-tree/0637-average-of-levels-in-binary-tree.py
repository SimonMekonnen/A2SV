# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        que = deque([root])
        ans = []
        while que:
            size = len(que)
            cur = 0
            for _ in range(size):
                now = que.popleft()
                cur += now.val
                if now.left:
                    que.append(now.left)
                if now.right:
                    que.append(now.right)
            ans.append(cur/size)
        return ans
                
                
        