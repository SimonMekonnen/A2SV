class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = -1 
        right = len(nums)
        
        while left + 1 < right:
            
            mid = (left + right)// 2
            
            if nums[mid] < target:
                left = mid
            
            else:
                right = mid
        
        r = right
        
        left = -1 
        right = len(nums)
        
        while left + 1 < right:
            
            mid = (left + right)// 2
            
            if nums[mid] <= target:
                left = mid
            
            else:
                right = mid
        
        if not nums or r >= len(nums) or nums[r] != target:
            return [-1, -1]
        else:
            return [r,left]
        
     
     


        
        