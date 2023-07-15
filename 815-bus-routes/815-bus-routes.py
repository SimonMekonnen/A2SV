class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if target == source:
            return 0
        for i in range(len(routes)):
            routes[i] = set(routes[i])
        
        graph = defaultdict(set)
  
        dic = defaultdict(set)
        for i in range(len(routes)):
            
            for j in routes[i]:
                dic[j].add(i)
                for k in range(i + 1,len(routes)):
                    if j in routes[k]:
                        graph[i].add(k)
                        graph[k].add(i)
        que = deque(dic[source])
        level = 1
        visited = [0 for i in range(len(routes))]
        while que:
            size = len(que)
            for i in range(size):
                now = que.popleft()
                for i in routes[now]:
                    if i == target:
                        return level
                for neigh in graph[now]:
                    if not visited[neigh]:
                        que.append(neigh)
                        visited[neigh] = 1
            level += 1
        return -1
        
        