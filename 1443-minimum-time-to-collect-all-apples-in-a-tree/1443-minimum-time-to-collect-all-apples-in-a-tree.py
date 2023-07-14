class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for i in range(n)]
        visited = [0 for i in range(n)]
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        ans = 0
        def dfs(node,parent):
            nonlocal ans
            if visited[node]:
                return 
            visited[node] = 1
            for neigh in graph[node]:
                dfs(neigh,node)
               
                
            if hasApple[node] == True:
                if node!=0:
                    ans += 2
                hasApple[parent] = True
                
      
        
            return
       
        dfs(0,0)
        return ans
        
        
            
            
        