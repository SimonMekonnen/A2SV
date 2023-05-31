class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0  for i in range(amount + 1)]
        dp[0] = 1
        for x in coins:
            for i in range(amount + 1):
                if i - x >= 0:
                    dp[i] += dp[i - x]       
        return dp[-1]
      
        