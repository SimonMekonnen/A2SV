class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        total = 0
        pre = {0 : 1}
        ans = 0
        for i in nums:
            
            total += i
            if total - goal in pre:
                ans += pre[total - goal]
            
            pre[total] = pre.get(total,0) + 1
        
        return ans
      