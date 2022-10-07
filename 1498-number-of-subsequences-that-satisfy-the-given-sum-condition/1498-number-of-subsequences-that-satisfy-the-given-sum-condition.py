class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        l = 0
        r =len(nums) - 1
        ans = 0
        nums.sort()
        while l <= r:
                if nums[l] + nums[r] <= target:
                    ans+=pow(2,(r - l),1000000007)
                    l+=1
                else: 
                    r-=1
        return ans%1000000007
        