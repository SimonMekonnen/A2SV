class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        s = sum(nums) // 2
        if sum(nums) % 2 == 1:
            return False
        memo = [[-1] * (s + 2)for i in range(len(nums))]
        def dp(index,total):
            if total < 0 or index >= len(nums):
                return False
            if memo[index][total] != -1:
                return memo[index][total]
            if total == 0:
                return True

            pick = dp(index + 1,total - nums[index])
            dont = dp(index + 1,total)
            memo[index][total] = pick or dont
            return memo[index][total]
        
        return dp(0,s)
        

       