class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        profit = 0
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] < nums[right]:
                profit = (max(profit,nums[right] - nums[left]))
            else:
                left = right
            right+=1
        return profit
        
    
        
                
        