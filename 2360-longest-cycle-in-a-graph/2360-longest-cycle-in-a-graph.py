class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        degree = [0 for i in range(len(edges))]
        que = deque()
        ans = 0
        for i in range(len(edges)):
            if edges[i]!= -1:
                degree[edges[i]] += 1
         
        for i in range(len(edges)):
            if degree[i] == 0:
                que.append(i)
     
        while que:
            now = que.popleft()
            if edges[now] != -1:
                degree[edges[now]] -= 1
                if degree[edges[now]] == 0:
                    que.append(edges[now])
        
        for i in range(len(edges)):
                count = 0
                n = i
                while  degree[n] != 0:
                    count += 1
                    degree[n] -= 1
                    n = edges[n]
                ans = max(ans,count)
        return ans if ans else -1
                
                
            
        
        
        
            
        
                
        
        
        