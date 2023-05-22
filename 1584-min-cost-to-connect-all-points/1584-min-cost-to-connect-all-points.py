class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(i + 1,len(points)):
                edges.append([i,j])
        
        edges.sort(key = lambda x : abs(points[x[0]][0] - points[x[1]][0]) + abs(points[x[0]][1] - points[x[1]][1]))
        
        parent = [i for i in range(len(points))]
        def find(x):
            cur = x
            while cur != parent[cur]:
                cur = parent[cur]
            
            while x != parent[x]:
                v = parent[x]
                parent[x] = cur
                x = v
            return cur
        def union(x,y):
            nonlocal ans
            xparent = find(x)
            yparent = find(y)
            if xparent == yparent:
                return 
            ans += abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
            parent[xparent] = yparent
        
        ans = 0
        for i in edges:
            union(i[0],i[1])
        
        return ans
            
        
        