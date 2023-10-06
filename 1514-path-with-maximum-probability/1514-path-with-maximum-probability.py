class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        ans = [0 for i in range(n)]
        graph = [[] for i in range(n)]
        i = 0
        for x, y in edges:
            graph[x].append([succProb[i],y])
            graph[y].append([succProb[i],x])
            i += 1
       
    
        ans[start] = 1
        que = [(-1,start)]
        while que:
            dist,x = heappop(que)
            for w,y in graph[x]:
                distance = -(dist) * w
    
                if distance > ans[y]:  
                    ans[y] = distance
                    heappush(que,(-distance,y))
        return ans[end]
             
        