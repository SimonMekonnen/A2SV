class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        right = 0
        left = 0
        while right < len(nums):
            cur = nums[right]
            b = right
            while right < len(nums) and cur == nums[right] :
                right+=1
            c = right - b
            if c > 1:
                c = 2
            while c > 0:
                nums[left] = cur
                left+=1
                c-=1
        return left

        
        
                
            
        