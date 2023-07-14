from typing import List
from collections import deque
class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        graph = [ [ ] for i in range(n)]
        degree = [0 for i in range(n)]
        
        for x,y in edges:
            graph[x - 1].append(y - 1)
            degree[y - 1] += 1
            
        
        que = deque()
        for i in range(n):
            if degree[i] == 0:
                que.append(i)
        
        ans = [0 for i in range(n)]
        level = 1
        while que:
            size = len(que)
            for i in range(size):
                cur = que.popleft()
                ans[cur] = level
                
                for neigh in graph[cur]:
                    degree[neigh] -= 1
                    if degree[neigh] == 0:
                        que.append(neigh)
            level += 1
        return ans
        
        
