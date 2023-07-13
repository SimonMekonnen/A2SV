class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        max_len = -1
        def dfs(node, coloring, numbering, count):
            nonlocal max_len
            if coloring[node] == 1:
                return
            
            if coloring[node] == 2:
                # print("cycle: ", node)
                max_len = max(max_len, count - numbering[node])
                return
            
            if edges[node] == -1:
                return
            
            coloring[node] = 2
            numbering[node] = count
            dfs(edges[node], coloring, numbering, count + 1)  
            coloring[node] = 1
            
        coloring = defaultdict(int)
        numbering = defaultdict(int)
        for node in range(len(edges)):
            dfs(node, coloring, numbering, 0)
        
        return max_len if max_len else -1
            