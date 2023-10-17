class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = [0 for i in range(sum(nums) + 1)]
        dp[0] = 1
        for i in nums:
            for j in range(sum(nums),-1,-1 ):
                if dp[j] == 1:
                    dp[j + i] = 1
        return dp[sum(nums) // 2] if sum(nums) % 2 == 0 else 0

       