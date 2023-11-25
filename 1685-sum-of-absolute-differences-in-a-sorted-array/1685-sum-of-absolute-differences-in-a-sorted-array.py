class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pre = [0]
        ans = []
        total = 0
        for i in range(len(nums)):
            total+=nums[i]
            pre.append(total)
        for i in range(1,len(pre)):
            before = nums[i-1] * (i - 1) - pre[i-1]
            after = pre[-1] - pre[i - 1] - (nums[i-1] * (len(pre)-i))
            ans.append(before + after)
        return ans




     
        