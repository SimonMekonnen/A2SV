class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = -1
        dic = {}
        for i,n in enumerate(nums):
            c = sum([int(b) for b in str(n)])
            if c in dic:
                ans = max(ans,nums[dic[c]] + n)
                if nums[dic[c]] < n :
                    dic[c] = i
            else:
                dic[c] = i
        return ans
 
        
        