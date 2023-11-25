class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        
        @cache
        def dp(index):
            if index >= len(prices):
                return 0
            
            ans = math.inf
            for i in range(index + 1, 2 * (index + 1) + 1):
                
                ans = min(ans,dp(i))
                
            return ans + prices[index]
    
        return dp(0)
    
