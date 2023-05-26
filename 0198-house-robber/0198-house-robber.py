class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(index ,memo = {}):
            if index in memo:
                return memo[index]
            if index >= len(nums):
                return 0
            memo[index] = nums[index] + max(dp(index + 2),dp(index + 3))
            return memo[index]
        
        return max(dp(0),dp(1))
        
        