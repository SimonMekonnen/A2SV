class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums = sorted(list(set(nums)))
        ans = n
        for i in range(len(nums)):
            ans = min(ans,i + (n - bisect_right(nums,nums[i]+ n - 1)))
        return ans
            
            
            
      
            
        
    