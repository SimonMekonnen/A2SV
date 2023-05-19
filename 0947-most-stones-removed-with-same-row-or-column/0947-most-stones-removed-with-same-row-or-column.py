class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        edges = []
        parent = {}
        ans = defaultdict(int)
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
        for i in stones:
            parent[tuple(i)] = tuple(i)
        for i in range(len(stones)):
            for j in range(i + 1,len(stones)):
                x1 = stones[i][0]
                x2 = stones[i][1]
                y1 = stones[j][0]
                y2 = stones[j][1]
                if x1 == y1 or x2 == y2:
                    union(tuple(stones[i]),tuple(stones[j]))

             
        
        for i in parent:
            parent[i] = find(i)
        
        for i in parent:
            ans[parent[i]] += 1
    
        return len(stones) - len(ans)
            
        
        
            
            
        
        
     
   