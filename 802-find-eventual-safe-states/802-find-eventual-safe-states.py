class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        que = deque()
        degree = [len(graph[i]) for i in range(len(graph))]
        edges = [[] for i in range(len(graph))]
           
        for i in range(len(degree)):
            if degree[i] == 0:
                que.append(i)
            for x in graph[i]:
                edges[x].append(i)
        ans = [0 for i in range(len(graph))]
        while que:
            cur = que.popleft()
            ans[cur] = 1
            for neigh in edges[cur]:
                degree[neigh] -= 1
                if degree[neigh] == 0:
                    que.append(neigh)
        real = []
        for i in range(len(ans)):
            if ans[i] == 1:
                real.append(i)
        return real
            
        
                
            
        
        