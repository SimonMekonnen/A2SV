class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        ans = set()
        for i in range(len(isConnected)):
            visited = set()
            def helper(start):
                nonlocal visited
                visited.add(start)
    
                for j in range(len(isConnected[start])):
                    
                    if isConnected[start][j] == 1 and (j not in visited):
                        helper(j)
            helper(i)
            ans.add(tuple(sorted(list((visited)))))
      
        return len(ans)
                        
                        
                        
                    