class Solution:
    def numSquares(self, n: int) -> int:
        
        arr = []
        for i in range(1,int(n ** 0.5) + 1):
            arr.append(i ** 2)
        
        dp = [inf for i in range(n + 1)]
        for i in arr:
            if i <= n:
                dp[i] = 1
        for i in range(2,len(dp)):
            for x in arr:
                if i - x >= 0:
                    dp[i] = min(dp[i],dp[i - x] + 1)
        return dp[-1]
        
        
        