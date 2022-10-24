class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        _sum = sum(nums)
        current = 0
        ans = 0
        for i in range(len(nums)-1):
            current+=nums[i]
            if current >= _sum - current:
                ans+=1
        return ans
        
        
        