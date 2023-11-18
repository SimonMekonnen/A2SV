class Solution:
    def minNumberOperations(self, nums: List[int]) -> int:
        
        last = nums[0]
        ans = 0
        op = 0
        for i in range(1,len(nums)):
            if last > nums[i]:
                ans += last - op
                op = nums[i]
            last = nums[i]
        if last != op:
            ans += last - op
        return ans