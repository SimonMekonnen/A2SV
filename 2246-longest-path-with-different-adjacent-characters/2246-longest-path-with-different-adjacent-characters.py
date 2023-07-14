class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        graph = [[] for i in range(len(parent))]
        for i in range(len(parent)):
            if parent[i] != -1:
                graph[parent[i]].append(i)
        
        ans = 1
        def dfs(node):
            nonlocal ans
            best = 0
            second = 0
            for neigh in graph[node]:
                now = dfs(neigh)
                if s[parent[neigh]] != s[neigh]:
                    if now > best:
                        second = best
                        best = now
                    elif now > second:
                        second = now

            ans = max(ans,best + second + 1)
            
            return best + 1
            
                
        dfs(0)
        return ans
         
                    
                
                
                
            
            
            