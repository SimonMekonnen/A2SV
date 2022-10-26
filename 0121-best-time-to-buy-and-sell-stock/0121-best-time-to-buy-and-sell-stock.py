class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        profit = 0
        left = 0
        right = 1
        while right < len(nums):
            profit = (max(profit,nums[right] - nums[left]))
            if nums[right] - nums[left] < 0:
                left = right
            right+=1
        return profit
        
    
        
                
        