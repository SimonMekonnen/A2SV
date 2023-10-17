class Solution:
    def mincostTickets(self, nums: List[int], costs: List[int]) -> int:
        
        @cache
        def dp(index):
            
            if index >= len(nums):
                return 0
            s = bisect_left(nums,nums[index] + 7)
            m = bisect_left(nums,nums[index] + 30)
            one = costs[0] + dp(index + 1)
            seven = costs[1] + dp(s)
            month = costs[2] + dp(m)
            return min(one,seven,month)
        return dp(0)
        
        
  