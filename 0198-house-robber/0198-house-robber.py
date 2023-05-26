class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(index):
            if index >= len(nums):
                return 0
            return nums[index] + max(dp(index + 2),dp(index + 3))
         
        
        return max(dp(0),dp(1))
        
        