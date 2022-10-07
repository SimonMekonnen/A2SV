class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        l = 0
        r =len(nums) - 1
        ans = 0
        nums.sort()
        while l <= r:
                if nums[l] + nums[r] <= target:
                    ans+=(2**(r - l)%1000000007)
                    l+=1
                else: 
                    if 2*nums[r] <= target:
                        ans+=1
                    r-=1
        return ans%1000000007
        