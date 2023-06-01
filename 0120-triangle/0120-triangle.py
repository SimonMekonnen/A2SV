class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:
        dp = [[inf for i in range(len(tri))] for i in range(len(tri))]
        dp[0][0] = tri[0][0]
        for row in range(len(dp) - 1):
            for col in range(len(tri[row])):
                dp[row + 1][col] = min(dp[row + 1][col],dp[row][col] + tri[row + 1][col])
                dp[row + 1][col + 1] = min(dp[row + 1][col + 1],dp[row][col] + tri[row + 1][col + 1])
        return min(dp[-1])

            
        