class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if target == source:
            return 0
        for i in range(len(routes)):
            routes[i] = set(routes[i])
        
        graph = defaultdict(set)
  
        postarget = set()
        possource = set()
        for i in range(len(routes)):
                now = routes[i]
                if target in now:
                    postarget.add(i)
                if source in now:
                    possource.add(i)
                for k in range(i + 1,len(routes)):
                        for j in routes[k]:
                            if j in now:
                                graph[i].add(k)
                                graph[k].add(i)
                                break
                
        que = deque(possource)
        level = 1
        visited = [0 for i in range(len(routes))]
        while que:
            size = len(que)
            for i in range(size):
                now = que.popleft()
                if now in postarget:
                    return level
                for neigh in graph[now]:
                    if not visited[neigh]:
                        que.append(neigh)
                        visited[neigh] = 1
            level += 1
        return -1
        
        