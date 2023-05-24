class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], aS: List[List[int]]) -> int:
        graph = defaultdict(lambda : defaultdict(int))
        parent = [i for i in range(len(source))]
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
            xparent = find(x)
            yparent = find(y)
            parent[xparent] = yparent
          
        for x,y in aS:
            union(x,y)
        
        for i in range(len(source)):
            graph[find(i)][source[i]] += 1
        count = 0
        for i in range(len(source)):
            now = graph[find(i)]
            if now[target[i]] != 0:
                now[target[i]] -= 1
            else:
                count += 1
        return count
        
        
        
            
        