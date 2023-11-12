class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0] * 2 ** k
        pre = [0]
        for i in nums:
            pre.append(pre[-1] | i)
        
        suf = [0]
        
        for i in nums[::-1]:
            suf.append(suf[-1] | i)
        
        suf.reverse()
        ans = 0
        suf.pop()
        pre.pop(0)
        t = 2 ** k
        
        for i in range(len(pre)):
            if i == 0:
                ans = max(suf[i + 1] | (nums[i] * t),ans)
            elif  i == len(pre) - 1:
                ans = max(pre[i - 1] | (nums[i] * t),ans)
            else:
                ans = max(pre[i - 1] | suf[i + 1] | (nums[i] * t),ans)
                
        return ans
     