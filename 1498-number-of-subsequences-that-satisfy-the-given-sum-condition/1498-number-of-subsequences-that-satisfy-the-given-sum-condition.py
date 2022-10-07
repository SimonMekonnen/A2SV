class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        nums.sort()
        ans = 0
        while left <= right:
            val = nums[left] + nums[right]
            if val > target:
                right-=1
            else:
                ans += pow(2,right-left,10**9+7)
                left+=1
        return ans % (10**9 + 7)