class Solution:
    def maxTurbulenceSize(self, nums: List[int]) -> int:
        def cmp(x, y):
            return (x > y) - (x < y)
        left = 0
        ans = 1
        for right in range(1,len(nums)):
            b = cmp(nums[right -1],nums[right])
            if b == 0:
                left = right
            elif right == len(nums) - 1 or b*cmp(nums[right],nums[right+1])!= -1:
                ans = max(ans,right - left + 1)
                left = right
        return ans
                
                
            
        
        
     