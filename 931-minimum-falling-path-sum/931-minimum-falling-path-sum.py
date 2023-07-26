class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        dp = [[inf for i in range(len(matrix))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            dp[0][i] = matrix[0][i]
        
        for row in range(len(matrix) - 1):
            for col in range(len(matrix)):
                if col - 1 >=0:
                    dp[row + 1][col - 1] = min(dp[row + 1][col -1],dp[row][col] + matrix[row + 1][col - 1])
                dp[row + 1][col] = min(dp[row + 1][col] ,matrix[row + 1][col] + dp[row][col])
                if col + 1 < len(matrix):
                    dp[row + 1][col + 1] = min(dp[row + 1][col + 1],matrix[row + 1][col + 1] + dp[row][col])
        return min(dp[-1])
                
        