class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        color = [0 for i in range(len(edges))]
        stack = {}
        ans = -1
        def dfs(node,length):
            nonlocal ans
            if color[node] == 2:
                return 
            if color[node] == 1:
                ans = max(ans,length - stack[node])
                return 
            color[node] = 1
            stack[node] = length
            
            if edges[node] != -1:
                dfs(edges[node],length + 1)
                
            color[node] = 2
            return 
        for i in range(len(edges)):
            if color[i] == 0:
                dfs(i,0)
        return ans
        
        