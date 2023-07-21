class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1,1] for i in range(len(nums))]
        mymax = 1
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    if dp[i][0] < dp[j][0] + 1:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    elif dp[i][0] == dp[j][0] + 1:
                        dp[i][1] += dp[j][1]
                    
            mymax = max(dp[i][0],mymax)
        ans = 0
        for x,y in dp:
            if x == mymax:
                ans += y
        return ans
                    