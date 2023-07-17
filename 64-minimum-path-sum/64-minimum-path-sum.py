class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        dp = [ [ inf for i in range(len(grid[0]))] for i in range(len(grid))]
        dp[0][0]=grid[0][0]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if col + 1 < len(grid[0]):
                    dp[row][col + 1] = min(dp[row][col + 1] , dp[row][col] + grid[row][col + 1])
                if row + 1 < len(grid):
                    dp[row + 1][col] = min(dp[row + 1][col] , dp[row][col] + grid[row + 1][col])
        return dp[-1][-1]
        