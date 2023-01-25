class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        last = nums[0]
        left = 1
        
        for i in range(1,len(nums)):
            
            if nums[i] != last:
                
                nums[left] = nums[i]
                last = nums[left]
                left+=1
                
        return left
            
    
            
        