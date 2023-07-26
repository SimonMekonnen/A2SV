class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = [[1,0] for i in range(len(nums))]
        
        for i in range(len(nums)):
            
            for j in range(i):
                
                if nums[i] - nums[j] > 0 and dp[j][1] <= 0 or nums[i] - nums[j] < 0 and dp[j][1] >= 0:
                    if dp[i][0] < dp[j][0] + 1:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = nums[i] - nums[j]
        ans = 0
        for x,y in dp:
            ans = max(ans,x)
        return ans
            
                        