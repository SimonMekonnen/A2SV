class Solution:
    def minMoves(self, nums: List[int]) -> int:
        t = min(nums)
        ans = 0
        for i in range(len(nums)):
            ans += nums[i] - t
        return ans