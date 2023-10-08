class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        
        a = nums[0]
        for i in nums:
            a &= i
        
        if a != 0:
            return 1
        t = nums[0]
        count = 0
        for i in range(len(nums)):
            t &= nums[i]
            if t == 0:
                count += 1
                if i + 1 < len(nums):
                    t = nums[i + 1]
        return count
        