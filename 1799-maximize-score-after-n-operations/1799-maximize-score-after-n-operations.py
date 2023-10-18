class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        @cache
        def dp(op,taken):
            if taken == 2**(len(nums) + 1) - 1:
                return 0
            ans = 0
            for i in range(len(nums)):
                for j in range(i + 1,len(nums)):
                    if (1 << i) & (taken) == 0  and( 1 << j) & taken == 0:
                        taken |= (1 << i)
                        taken |= (1 << j)
                        ans = max(ans,op * gcd(nums[i],nums[j]) + dp(op + 1,taken))
                        taken ^= (1 << i)
                        taken ^= (1 << j)
                
            return ans
        return dp(1,0)
                    
                    
        