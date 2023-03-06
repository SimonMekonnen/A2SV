class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stk = []
        ans = [-1 for i in nums]
        nums = nums + nums
        for i in range(len(nums)):
            i %=n
            while stk and nums[stk[-1]] < nums[i]:
                c = stk.pop()
                ans[c] = nums[i]
            stk.append(i)
        return ans
                
                
       
                    
                
   
                