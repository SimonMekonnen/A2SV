class Solution:
    def validMountainArray(self, nums: List[int]) -> bool:
        
        flag = 1
        for i in range(len(nums) - 1):
            if (i == 0 and nums[i] > nums[i + 1] )or (nums[i] == nums[i + 1]):
                
                return False
            
            if flag ==  0 and nums[i] < nums[i + 1]:
                
                return False
            
            if nums[i] > nums[i + 1]:
                
                flag = 0
        
        if flag == 1:
            
            return False
        
        return True
            
            
           
        
        
        
        
        