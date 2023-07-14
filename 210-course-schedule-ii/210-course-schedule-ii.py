class Solution:
    def findOrder(self, c: int, p: List[List[int]]) -> List[int]:
        graph = [[] for i in range(c)]
        degree = [0 for i in range(c)]
        for x,y in p:
            degree[x] += 1
            graph[y].append(x)
        
        que = deque()
        for i in range(len(degree)):
            if degree[i] == 0:
                que.append(i)
        
        ans = []
        while que:
            now = que.popleft()
            ans.append(now)
            for neigh in graph[now]:
                degree[neigh] -= 1
                if degree[neigh] == 0:
                    que.append(neigh)
        if len(ans) == c:
            return ans
        else:
            return []
        