class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        
        dp = [[0] * len(grid[0]) for i in range(len(grid))]
        if grid[0][0] == 0:
            dp[0][0] = 1 
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                down = i + 1
                right = j + 1
                
                if i + 1 < len(grid) and grid[i + 1][j] == 0:
                    dp[down][j] +=dp[i][j]
                
                if right < len(grid[0]) and grid[i][right]  == 0:
                    dp[i][right] += dp[i][j]
    
        return dp[-1][-1]