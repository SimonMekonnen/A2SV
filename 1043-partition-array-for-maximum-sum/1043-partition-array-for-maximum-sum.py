class Solution:
    def maxSumAfterPartitioning(self, nums: List[int], k: int) -> int:
        dp = [0 for i in range(len(nums)+1)]
        for i in range(len(nums)):
            count = 1
            m = nums[i]
            for j in range(i,max(-1,i - k),-1):
                m = max(nums[j],m)
                dp[i + 1] = max(dp[i + 1],m * count + dp[j])
                count += 1    
        return dp[-1]
        
