class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        dp = [[float('-inf') for _ in range(m + 1)] for _ in range(n + 1)]
        dp[n - 1][m - 1] = dungeon[-1][-1]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i == n - 1 and j == m - 1:
                    continue
                dp[i][j] = min(dungeon[i][j], dungeon[i][j] + max(dp[i + 1][j], dp[i][j + 1]))
        return -1 * min(0,dp[0][0]) + 1

