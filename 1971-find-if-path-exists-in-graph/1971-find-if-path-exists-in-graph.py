class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        parent = [i for i in range(n)]
        size = [1 for i in range(n)]
        def find(v):
            cur = v
            while cur != parent[cur]:
                cur = parent[cur]     
            return cur
        
        def union(v1,v2):
            parentv1= find(v1)
            parentv2 = find(v2)
            if size[v1] > size[v2]:
                parent[parentv1] = parentv2
                size[parentv1] += size[parentv2]
            else:
                parent[parentv2] = parentv1
                size[parentv2] += size[parentv1]
                
            
        for v1 , v2 in edges:
            union(v1,v2)
        return find(source) == find(destination)
        