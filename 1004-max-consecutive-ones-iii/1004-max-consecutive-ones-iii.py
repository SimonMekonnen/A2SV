class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        ans = 0
        while r <  len(nums):
            if nums[r] == 1 or k > 0:
                k-= nums[r]==0
                r+=1
            else:
                k+=nums[l]==0
                l+=1
            ans = max(ans,r - l)
        return ans
                
                
        