class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pre = [nums[0]]
        for i in range(1,len(nums)):
            pre.append(pre[-1]+nums[i])
        ans = 0
        for i in range(len(nums)-1):
            if pre[i] >= (pre[-1] -pre[i]):
                ans+=1
        return ans
        
        
        