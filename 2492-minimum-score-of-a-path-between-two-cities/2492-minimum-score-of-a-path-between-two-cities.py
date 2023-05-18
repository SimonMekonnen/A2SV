class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        for x,y,d in roads:
            graph[x].add((y,d))
            graph[y].add((x,d))
            
        que = deque([1])
        ans = []
        visited = set()
        visited.add(1)
        while que:
            cur = que.popleft()
            visited.add(cur)
            for neigh in graph[cur]:
                if neigh[0] not in visited:
                    que.append(neigh[0])    
                    ans.append(neigh[1])
          
        
        return min(ans)
            
        
        
        
        