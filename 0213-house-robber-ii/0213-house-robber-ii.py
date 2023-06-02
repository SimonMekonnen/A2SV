class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        @cache
        def dp(index,n):
            if index >= n:
                return 0
            return max(nums[index] + dp(index + 2,n),dp(index + 1,n))
        return max(dp(0,len(nums) - 1),dp(1,len(nums)))
        
        