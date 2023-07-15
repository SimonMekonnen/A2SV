class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if target == source:
            return 0
        for i in range(len(routes)):
            routes[i] = set(routes[i])
        
        graph = defaultdict(set)
  
        postarget = set()
        possource = set()
        for i, r1 in enumerate(routes):
            if source in r1:
                possource.add(i)
            if target in r1:
                postarget.add(i)
            for j in range(i+1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)
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
        
        