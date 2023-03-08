class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def helper(right,left,score,turn):
            if right < left:
                
                return score >= 0
            
            elif turn == 1:
                
                return helper(right - 1,left,score + nums[right],0) or helper(right,left + 1,score + nums[left],0)
            else:
                return helper(right - 1,left,score - nums[right],1) and helper(right,left + 1,score - nums[left],1)
        
        
        return helper(len(nums) - 1,0,0,1)
                
        