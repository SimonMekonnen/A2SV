class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = nums[0]
        total = nums[0]
        for i in range(1,len(nums)):
            total += nums[i]
            if ans < math.ceil(total / (i + 1)):
                ans = math.ceil(total / (i + 1))
        return ans
            
            
            
        