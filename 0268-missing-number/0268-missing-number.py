class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            while nums[i] != i:
                
                if nums[i] > len(nums) - 1:
                    break
                nums[nums[i]] ,nums[i] = nums[i], nums[nums[i]]
                
        for i in range(len(nums)):
            if nums[i] != i:
                return i
            
        return nums[-1] + 1
            
        
        