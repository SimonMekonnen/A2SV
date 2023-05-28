class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [0,0,1,0]
        
        for i in range(2,n + 1):
            if i % 2 == 1:
                dp.append(1 - dp[i - 1])
            else:
                if dp[i - 1] * dp[i - 2] == 0:
                    dp.append(1)
                else:
                    dp.append(0)
        return dp[n]
        