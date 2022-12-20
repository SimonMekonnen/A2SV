class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i,n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue 
            left = i + 1
            right = len(nums) -  1
            while left <  right:
                tsum = nums[left] + nums[right] + n
                if tsum > 0:
                    right-=1
                elif tsum < 0:
                    left+=1
                else:
                    ans.append([n,nums[left],nums[right]])
                    left+=1
                    while nums[left] == nums[left - 1] and left < right:
                        left+=1
        return ans
            
           
        
        
            
            
        