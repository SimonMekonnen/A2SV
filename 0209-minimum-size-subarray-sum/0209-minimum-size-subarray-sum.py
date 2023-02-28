class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l , mn, total =  0, len(nums) + 1, 0
        for r in range(len(nums)):
            total+=nums[r]
            while total >= target:
                mn = min(mn,r - l + 1)
                total-=nums[l]
                l+=1
        return mn if mn != len(nums) + 1 else 0







            
            
        
        