class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        parent = [i for i in range(n)]
        def find(x):
            if parent[x] == x:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]
        ans = []   
        for x, y in requests:
            xparent = find(x)
            yparent = find(y)
            pos = True
            for i,j in restrictions:
                ip = find(i)
                jp = find(j)
                if  sorted([jp,ip]) == sorted([xparent,yparent]):
                    pos = False
            if pos:
                parent[xparent] = yparent
            ans.append(pos)
        return ans

            
            