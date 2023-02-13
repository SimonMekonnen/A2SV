class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        k = 0
        s = 1
        for i in range(len(nums)):
            if nums[i] > 0:
                ans[k] = nums[i]
                k+=2
            else:
                ans[s] = nums[i]
                s+=2
        return ans


        