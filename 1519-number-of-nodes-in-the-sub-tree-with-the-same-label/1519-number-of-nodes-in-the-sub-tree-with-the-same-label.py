class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = defaultdict(set)
        for x,y in edges:
            graph[x].add(y)
            graph[y].add(x)
        
        ans = [0] * n
        
        visited = set()
        
        def dfs(node, count):
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    res = dfs(child, [0 for _ in range(26)])
                    for i in range(26):
                        count[i] += res[i]
                    
                        
            idx = ord(labels[node]) - ord('a')
            count[idx] += 1
            ans[node] = count[idx]
            return count
        dfs(0, [0 for _ in range(26)])
        return ans
            
            
        # def dfs(node):
#             nonlocal n
#             for child in graph[node]:
#                 if child not in visited:
#                     visited.add(child)
#                     now = dfs(child)
#                     now[labels[child]] += 1
#                     ans[node] = now[labels[node]]
#                     return now
                    
                    
#             return defaultdict(int)
                  
                    
         
#         dfs(0)
#         return ans
            
            
            
            
            