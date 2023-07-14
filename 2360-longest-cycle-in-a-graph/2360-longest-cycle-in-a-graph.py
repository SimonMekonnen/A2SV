class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        colors = [0 for _ in range(n)]
        stack = {}
        ans = 0
        def dfs(node, i):
            nonlocal ans
            if colors[node] == 1:
                ans = max(ans, i - stack[node])
                return 
            if colors[node] == 2:
                return 
            
            stack[node] = i
            colors[node] = 1
            if edges[node] != -1:
                
                dfs(edges[node], i + 1)
            
#             del stack[node]
            
            colors[node] = 2
            return 
        
        for i in range(n):
            if not colors[i]:
                dfs(i, 0)
        return ans if ans else -1
                
        