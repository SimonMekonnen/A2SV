class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dp(idx): 
             
            if idx  in memo: 
                return memo[idx] 
 
            if idx == 0: 
                return nums[0] 
 
            if idx == 1: 
                return max(nums[0], nums[1]) 
 
             
            memo[idx] = max(dp(idx - 1), nums[idx] + dp(idx-2)) 
            return memo[idx] 
             
 
        return dp(n - 1)
        
        