class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(set)
        count = [0 for i in range(len(quiet))]
        why = defaultdict(set)
        def bfs(x):
            que = deque([x])
            visited = set([x])
            while que:
                cur = que.popleft()
                visited.add(cur)
                for neigh in why[cur]:
                    if neigh not in visited:
                        que.append(neigh)
                        visited.add(neigh)
            return visited
                    
                
        for x,y in richer:
            graph[x].add(y)
            why[y].add(x)
            count[y] += 1
        
        
        level = []
        que = deque()
        for i in range(len(count)):
            if count[i] == 0:
                que.append(i)
        while que:
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                level.append(cur)
                for neigh in graph[cur]:
                    count[neigh] -= 1
                    if count[neigh] == 0:
                        que.append(neigh)
    
    
        res = [i for i in range(len(quiet))]
        for i in range(len(quiet)):
            v = bfs(level[i])
            ans = quiet[level[i]]
            index = level[i]
            for j in range(0,i+1):
                if level[j] in v and quiet[level[j]] < ans:
                    index = level[j]
                    ans = quiet[level[j]]
            res[level[i]] = index
        
        return res
                
        
        
                