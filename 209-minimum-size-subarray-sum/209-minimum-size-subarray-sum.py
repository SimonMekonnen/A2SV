class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        summ = 0
        ans = math.inf
        for i in range(len(nums)):
            summ+=nums[i]
            while summ >= target:
                ans = min(ans,i - start + 1)
                summ-=nums[start]
                start+=1
        return ans if ans != math.inf else 0
            
            
            
        
        