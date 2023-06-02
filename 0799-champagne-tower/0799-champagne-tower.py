class Solution:
    def champagneTower(self, poured: int, r: int, glass: int) -> float:
        dp = [[0 for i in range(100)] for i in range(100)]
        
        dp[0][0] = poured
        for row in range(99):
            for col in range(row + 1):
                if dp[row][col] > 1:
                    toshare = dp[row][col] - 1
                    dp[row][col] = 1
                    dp[row + 1][col] += (toshare/2)
                    dp[row + 1][col + 1] += (toshare/2)
        return dp[r][glass]
                    
        