class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        parent = [i for i in range(n)]
        def find(x):
            cur = x
            while cur != parent[cur]:
                cur = parent[cur]
            while x != parent[x]:
                v = parent[x]
                parent[x] = cur
                x = v
            return cur
        ans = []   
        for x, y in requests:
            xparent = find(x)
            yparent = find(y)
            pos = True
            for i,j in restrictions:
                ip = find(i)
                jp = find(j)
                if  (jp == xparent and ip == yparent) or (jp == yparent and ip == xparent):
                    pos = False
                    break
            if pos:
                parent[xparent] = yparent
            ans.append(pos)
        return ans

            
            