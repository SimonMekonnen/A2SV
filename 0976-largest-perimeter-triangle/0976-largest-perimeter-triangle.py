class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        right = 2
        ans = 0
        
        while right < len(nums):
            if nums[right - 1] + nums[right - 2] > nums[right]:
                ans = nums[right - 1] + nums[right - 2] + nums[right]
                
            right+=1
        
        return ans
        
        
        