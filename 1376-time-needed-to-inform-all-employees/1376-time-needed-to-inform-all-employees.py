class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(set)
        for i in range(len(manager)):
            if manager[i] != -1:
                graph[manager[i]].add(i)
        que = deque([headID])
        ans = 0
        while que:
            size = len(que)
            time = 0
            for i in que:
                time = max(time,informTime[i])
            for i in range(size):
                cur = que.popleft()
                for neigh in graph[cur]:
                    que.append(neigh)
                    informTime[neigh] -= (time - informTime[cur])
            ans += time
        return ans
            
        