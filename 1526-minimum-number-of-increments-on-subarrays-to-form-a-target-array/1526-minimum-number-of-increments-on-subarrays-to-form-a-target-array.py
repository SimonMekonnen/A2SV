class Solution:
    def minNumberOperations(self, nums: List[int]) -> int:
        
    
       
        
        stk = []
        ans = 0
        op = 0
        for i in range(len(nums)):
            if stk and stk[-1] > nums[i]:
                ans += stk[-1] - op
                stk = []
                op = nums[i]
            stk.append(nums[i])
        if stk:
            ans += stk[-1] - op
        return ans