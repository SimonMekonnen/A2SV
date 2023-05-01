class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        direction = [[0,-1],[0,1],[1,0],[-1,0]]
        m = len(grid)
        n = len(grid[0])
        visited = set()
        def dfs(z,k):
            nonlocal count
            if grid[z][k] == 0:
                return 
           
            for x,y in direction:
                newx = z + x
                newy =  k + y
                if 0 <= newx < m and 0 <= newy < n and (newx,newy) not in visited and grid[newx][newy] == 1:
                    visited.add((newx,newy))
                    count += 1
                    dfs(newx,newy)
        ans = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row,col) not in visited:
                    count = 1
                    visited.add((row,col))
                    dfs(row,col)
                    ans = max(ans,count)
        return ans
                    
     
        
        
            
        