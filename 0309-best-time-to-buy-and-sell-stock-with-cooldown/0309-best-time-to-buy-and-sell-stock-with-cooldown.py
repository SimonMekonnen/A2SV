class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(index,buy):
            if index >= len(prices):
                return 0
       
            
            if not buy:
                 buy = dp(index + 1,1) - prices[index]
                 notbuy = dp(index + 1,0)
                 return max(buy,notbuy)
            if buy:
                sell = dp(index + 2,0) + prices[index]
                notsell = dp(index + 1,1)
                return max(sell, notsell)
                
           
        return dp(0,0)
        