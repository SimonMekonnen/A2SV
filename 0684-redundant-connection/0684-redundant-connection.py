class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges) + 1)]
        ans = []
        for x,y in edges:
            parentx = parent[x]
            parenty = parent[y]
            x,y
            if parentx == parenty:
                ans.append([x,y])
            
            else:
                for i in range(len(parent)):
                    if parent[i] == parenty:
                        parent[i] = parentx
        return ans[-1]
            
            
            
        
        