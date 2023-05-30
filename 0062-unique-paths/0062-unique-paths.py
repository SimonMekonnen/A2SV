class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for i in range(m)]
        dp[0][0] = 1
        for row in range(m):
            for col in range(n):
                if row + 1 < m:
                    dp[row + 1][col] += dp[row][col]
                if col + 1 < n:
                    dp[row][col + 1] += dp[row][col]         
        return dp[-1][-1]
        