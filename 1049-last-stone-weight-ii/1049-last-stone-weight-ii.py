class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
    
        dp = [[0] * 6002 for i in range(len(stones)) ]
        dp[0][stones[0] + 3000] = 1
        dp[0][-stones[0] + 3000] = 1
        
        for i in range(len(dp) - 1):
            for j in range(6001):
                if dp[i][j] == 1:
                        dp[i + 1][j + stones[i + 1]] = 1
                        dp[i + 1][j - stones[i + 1]] = 1
        for i in range(3000,len(dp[0])):
            if dp[-1][i] == 1:
                return i - 3000
            