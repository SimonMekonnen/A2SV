class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        ans = [inf for i in range(n)]
        graph = [[] for i in range(n)]
        for i in range(len(times)):
            graph[times[i][0] - 1].append((times[i][2] ,times[i][1] - 1))
    
        ans[k - 1] = 0
        que = [(0,k - 1)]
        while que:
            dist,x = heappop(que)
            for w,y in graph[x]:
                distance = dist + w
                if distance < ans[y]:
                    ans[y] = distance
                    heappush(que,(distance,y))
        
                    
        return max(ans) if max(ans) != inf else -1