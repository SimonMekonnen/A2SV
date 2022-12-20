class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right , d,ans = 0 , 0 , 0,0
        while right <  len(nums):
            if nums[right] ==  1 or d == 0:
                d+=nums[right]==0
                right+=1
            else:
                d-=nums[left]==0
                left+=1
            ans = max(ans,right-left)
        return ans - 1
            
        