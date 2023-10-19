class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        def valid(x,y):
            if x == y:
                return True
            if len(x) != len(y):
                return False
            arr = []
            for i in range(len(x)):
                if x[i] != y[i]:
                    arr.append(sorted([x[i],y[i]]))
            
            if len(arr) != 2:
                return False
            if arr[0] != arr[1]:
                return False
            return True
        
        
        parent = [i for i in range(len(strs))]
        size = [1 for i in range(len(strs))]
        def find(x):
            cur = x
            while parent[cur] != cur:
                cur = parent[cur]
            
            while parent[x] != cur:
                v = parent[x]
                parent[x] = cur
                x = v
            
            return cur
        
        def union(x,y):
            parentx = find(x)
            parenty = find(y)
            if size[parentx] <= size[parenty]:
                parent[parentx] = parenty
                size[parenty] += size[parentx]
            else:
                parent[parenty] = parentx
                size[parentx] += size[parenty]
                
            
        
        for i in range(len(strs)):
            for j in range(i + 1,len(strs)):
                if valid(strs[i],strs[j]):
                    union(i,j)
        for i in range(len(strs)):
            find(i)
        
        return len(set(parent))
                
            
            
                    
        