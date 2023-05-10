# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stk = [(1,root)]
        table = defaultdict(int)
        def childs(i):
            lc = 2*i
            rc = 2*i + 1
    
            return [2*lc,2*lc + 1,2*rc,2*rc + 1]
       
        while stk:
            cur = stk.pop()
            table[cur[0]] = cur[1].val
            if cur[1].left:
                stk.append((2*cur[0],cur[1].left))
            if cur[1].right:
                stk.append((2*cur[0] + 1,cur[1].right))
        count = 0
        
        for i in table:
            if table[i] % 2 == 0:
                c = childs(i)
                print(c)
                for j in c:
                    if j in table:
                        count += table[j]
        return count
        
        