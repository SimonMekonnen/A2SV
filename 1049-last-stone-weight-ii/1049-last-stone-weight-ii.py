class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
       @cache
       def dp(index,total):
            if index >= len(stones):
                return total if total >= 0 else inf
            
            add = dp(index + 1,total + stones[index])
            sub = dp(index + 1,total - stones[index])
            return min(add,sub)
        
       return dp(0,0)
            
            