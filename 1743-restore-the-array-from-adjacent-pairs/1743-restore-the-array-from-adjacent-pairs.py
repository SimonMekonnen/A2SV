class Solution:
    def restoreArray(self, a: List[List[int]]) -> List[int]:
        
        graph = defaultdict(set)
        for x,y in a:
            graph[x].add(y)
            graph[y].add(x)
        
        que = deque()
        for i in graph:
            if len(graph[i]) == 1:
                que.append(i)
                break
        ans = []
        while que:
            cur = que.popleft()
            ans.append(cur)
            for neigh in graph[cur]:
                graph[neigh].remove(cur)
                if len(graph[neigh]) == 1:
                    que.append(neigh)
        for i in graph:
            if len(graph[i]) == 0:
                ans.append(i)
        return ans
        