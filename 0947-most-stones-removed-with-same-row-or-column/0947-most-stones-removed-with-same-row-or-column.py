class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        edges = []
        parent = {}
        ans = defaultdict(int)
        for i in range(len(stones)):
            parent[tuple(stones[i])] = tuple(stones[i])
            for j in range(i + 1,len(stones)):
                x1 = stones[i][0]
                x2 = stones[i][1]
                y1 = stones[j][0]
                y2 = stones[j][1]
                if x1 == y1 or x2 == y2:
                    edges.append((tuple(stones[i]),tuple(stones[j])))

        def find(x):
            cur = x
            while cur != parent[cur]:
                cur = parent[cur]
            
            while x != parent[x]:
                 n = parent[x]
                 parent[x] = cur
                 x = n

            return cur
 
        def union(x,y):
            xparent = find(x)
            yparent = find(y)
            parent[xparent] = yparent
    
        for x,y in edges:
            union(x,y)
        
        for i in parent:
            parent[i] = find(i)
        
        for i in parent:
            ans[parent[i]] += 1
    
        return len(stones) - len(ans)
            
        
        
            
            
        
        
     
   