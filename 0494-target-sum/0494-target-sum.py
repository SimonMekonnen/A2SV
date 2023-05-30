class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [[0 for i in range(2001)] for i in range(len(nums))]
        dp[0][nums[0] + 1000] += 1
        dp[0][-nums[0] + 1000] += 1 
        for row in range(len(nums) - 1):
            for col in range(len(dp[0])):
                if dp[row][col] != 0:
                    dp[row + 1][col + nums[row + 1]] += dp[row][col]
                    dp[row + 1][col - nums[row + 1]] += dp[row][col]
        
        return dp[-1][target + 1000]
            
        