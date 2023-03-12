# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        que = deque([[root,1]])
        ans = []
        while que:
            
            cur = []
            b = set()
            for i in range(len(que)):
                
                curr = que.popleft()
                cur.append([curr[0].val,curr[1]])
                if curr[0].left:
                    que.append([curr[0].left , curr[1] * 2] )
                if curr[0].right:
                    que.append([curr[0].right,curr[1] * 2 + 1] )
       
          
            ans.append(cur)  
        _max = 0
        for i in ans:
            _max = max(i[-1][-1] - i[0][1] + 1,_max)
        
        return _max