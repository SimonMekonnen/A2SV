class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        visited = set()
        n = len(graph) - 1
        def dfs(s,arr):
            nonlocal n
            if s == n:
                arr.append(n)
                ans.append(arr.copy())
                return 
            arr.append(s)
            for child in graph[s]:
                if child not in visited:
                    visited.add(child)
                    dfs(child,arr)
                    visited.remove(child)
                    arr.pop()
        
        dfs(0,[])
        return ans
        
                
                
                    
        