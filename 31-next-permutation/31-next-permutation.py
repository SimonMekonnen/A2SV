class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
    
        """
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i-=1
        if i == 0:
            nums.reverse()
        else:
            while j > 0 and nums[j]<=nums[i - 1]:
                j-=1
            nums[i - 1],nums[j] = nums[j],nums[i - 1]
            l = i
            r = len(nums) - 1
            while l <= r:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1

                
        
        
                    
            
                
        
        