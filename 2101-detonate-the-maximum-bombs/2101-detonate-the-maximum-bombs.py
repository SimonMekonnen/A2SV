class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = [set() for i in range(len(bombs))]
        
        for i in range(len(bombs)):
            x,y,r = bombs[i]
        
            for j in range(len(bombs)):
                newx,newy,newr = bombs[j]
                if j != i:
                    if r**2 >= (x - newx)**2 + (y - newy)**2:
                        graph[i].add(j)
        def dfs(source):
            stk = [source]
            visited = set([source])
            while stk:
                cur = stk.pop()
                for i in graph[cur]:
                    if i not in visited:
                        stk.append(i)
                        visited.add(i)
            return len(visited)
        ans = 1
        for i in range(len(bombs)):
            ans = max(ans,dfs(i))
        return ans
            
            
                    
            
        