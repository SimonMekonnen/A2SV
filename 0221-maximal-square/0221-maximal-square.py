class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix[0])
        n = len(matrix)
        dp = [[0] * m for i in range(n)]
        ans = 0
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == "1":
                    var = inf
                    dp[row][col] += 1
                    if row - 1 >= 0:
                        var = min(var,dp[row - 1][col])
               
                    if col - 1 >= 0:
                        var = min(var,dp[row][col - 1])
                   
                    if row - 1 >= 0 and col - 1 >= 0:
                        var = min(var,dp[row - 1][col - 1])
                    else:
                        var = 0
                    
                    if var != inf:
                        dp[row][col] += var
                ans = max(dp[row][col],ans)
   
        return ans * ans
                    
        