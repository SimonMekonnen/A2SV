class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        incycle = [1 for i in range(len(edges))]
        degree = [0 for i in range(len(edges))]
        que = deque()
        visited = [0 for i in range(len(edges))]
        ans = 0
        for i in range(len(edges)):
            if edges[i]!= -1:
                degree[edges[i]] += 1
         
        for i in range(len(edges)):
            if degree[i] == 0:
                que.append(i)
     
        while que:
            now = que.popleft()
            incycle[now] = 0
            if edges[now] != -1:
                degree[edges[now]] -= 1
                if degree[edges[now]] == 0:
                    que.append(edges[now])
       
        def dfs(node,count):
            nonlocal ans
            if visited[node] == 1:
                ans = max(ans,count)
                return 
            visited[node] = 1
            if edges[node] != -1:
                dfs(edges[node],count + 1)
            
            return
        
        for i in range(len(edges)):
            if visited[i] != 1 and incycle[i] == 1:
                count = 1
                n = i
                while  edges[n] != i:
                    count += 1
                    visited[n] = 1
                    n = edges[n]
                ans = max(ans,count)
        return ans if ans else -1
                
                
            
        
        
        
            
        
                
        
        
        