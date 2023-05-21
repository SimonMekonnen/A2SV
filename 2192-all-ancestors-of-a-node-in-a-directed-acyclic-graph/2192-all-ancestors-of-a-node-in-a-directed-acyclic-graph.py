class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        for x,y in edges:
            graph[y].add(x)
        
        def bfs(x):
            que = deque([x])
            visited = set()
            while que:
                cur = que.popleft()
                visited.add(cur)
                for neigh in graph[cur]:
                    if neigh not in visited:
                        que.append(neigh)
                        visited.add(cur)
            return visited
        ans = []
        for i in range(n):
            c = bfs(i)
            c.remove(i)
            ans.append(sorted(c))
            
        return ans
        