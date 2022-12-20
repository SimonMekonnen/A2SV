class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left , ans, right = 0 , 0 , 0
        fliped = 0
        while right < len(nums):                 
            if nums[right] == 1:                         
                right += 1                                 
                                                    
            elif nums[right] == 0:                 
                while fliped >= k:
                    if nums[left] == 0:
                        fliped -= 1
                    left+=1
                if fliped < k:
                    fliped += 1
                    right += 1
                    
            ans = max(ans,right - left)
            
        return ans
                
                
                
                
                
        
        
        
        
   
                
                
        