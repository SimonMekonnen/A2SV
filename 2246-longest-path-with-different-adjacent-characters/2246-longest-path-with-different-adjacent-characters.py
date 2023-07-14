class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        graph = [[] for i in range(len(parent))]
        for i in range(len(parent)):
            if parent[i] != -1:
                graph[parent[i]].append(i)
        
        ans = 1
        def dfs(node):
            arr = []
            nonlocal ans
            for neigh in graph[node]:
                now = dfs(neigh)
                if s[parent[neigh]] != s[neigh]:
                    arr.append(now)
            
            if len(arr) >= 2:
                arr.sort()
                best = arr.pop()
                second = arr.pop()
                ans = max(ans,best + second + 1)
                return best + 1
            if len(arr) == 1:
                best = arr.pop()
                ans = max(ans,best + 1)
                return best + 1
            
            else:
                return 1
            
                
        dfs(0)
        return ans
         
                    
                
                
                
            
            
            