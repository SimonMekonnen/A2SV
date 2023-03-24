class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        i = 0
        while i < len(nums):
            if nums[i] >= len(nums):
                i += 1
                continue 
            if nums[i] <= 0:
                nums[0],nums[i] = nums[i],nums[0]
                i += 1
            elif nums[i] != i:
                b = 0
                if nums[i] == nums[nums[i]]:
                    b = 1
                nums[nums[i]] ,nums[i] = nums[i],nums[nums[i]]
                if b:
                    i += 1  
            else:
                i += 1
      
        if len(nums) == 1:
            return 1 if nums[0] !=  1 else 2
        for i in range(1,len(nums)):
            if nums[i] != i:
                return i
            if i == (len(nums) - 1) and nums[i] + 1 != nums[0]:
                return nums[i] + 1
        return max(nums) + 1