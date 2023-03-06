class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        total = 0
        ans = 0
        left = 0
        for right in range(len(nums)):
            total += nums[right]
            while left <= right and total >= goal:
                total -= nums[left]
                left += 1
            
            ans += right - left + 1
        
        total = 0
        ans2 = 0
        left = 0
        for right in range(len(nums)):
            total += nums[right]
            while left <= right and total > goal:
                total -= nums[left]
                left += 1
            
            ans2 += right - left + 1
    
        return ans2 - ans
        
        
        
        
       
      