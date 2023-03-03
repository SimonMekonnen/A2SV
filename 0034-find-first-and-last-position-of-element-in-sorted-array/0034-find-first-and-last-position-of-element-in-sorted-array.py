class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        b = bisect_left(nums,target)
        c = bisect_right(nums,target)
        
        ans = []
        if b >= len(nums) or nums[b] != target:
            return [-1,-1]
        else:
            return [b,c - 1]
            
     


        
        