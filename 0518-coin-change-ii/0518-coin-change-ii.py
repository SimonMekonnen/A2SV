class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        @cache
        def dp(target,index):
            if target == 0:
                return 1
            if target < 0 or index >= len(coins):
                return 0
            
            pick = dp(target - coins[index],index)
            dontpick = dp(target,index + 1)
            return pick + dontpick
        return dp(amount,0)
        