class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        total = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                total+=1
            else:
                total = 0
            ans = max(total,ans)
        return ans
            
     
            
            
            
        