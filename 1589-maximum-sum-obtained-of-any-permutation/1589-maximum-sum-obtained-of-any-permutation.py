class Solution:
    def maxSumRangeQuery(self, nums: List[int], r: List[List[int]]) -> int:
        
        pre = [0] * 100004
        
        for s,e in r:
            pre[s] += 1
            pre[e + 1] -= 1
        
        for i in range(1,len(pre)):
            pre[i] += pre[i - 1]
        
        new = sorted(nums,reverse = True)
        
        index = [i for i in range(len(pre))]
        index.sort(key = lambda x:pre[x],reverse = True)
        
        for i in range(len(new)):
            
            nums[index[i]] = new[i]
        
        for i in range(1,len(nums)):
            
            nums[i] += nums[i - 1]
        
        ans = 0
        
        for s,e in r:
            n = nums[s - 1] if s != 0 else 0
            ans += nums[e] - n
        
        return ans % (10**9 + 7)
        
        
        
        