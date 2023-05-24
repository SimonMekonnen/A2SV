class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        
        if len(nums) <= 3:
            return 0
        
        left = 0
        right = len(nums) - 1
        l = 3
        r = len(nums) - 4
        for i in range(3):
           
            if right - left + 1 == 3:
                if i == 1:
                    return 0
                if i == 2:
                    return min(nums[right] - nums[right - 1] ,nums[left + 1] - nums[left])
    
            if nums[r] - nums[left] < nums[right] - nums[l]:
                right -= 1
                l -= 1
            else:
                r += 1
                left += 1
        

        return nums[right] - nums[left]
                
        