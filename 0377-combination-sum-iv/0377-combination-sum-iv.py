class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for i in range(0,target + 1):
            for x in nums:
                if i + x < len(dp):
                    dp[i + x] += dp[i]
        return dp[-1]
                
        