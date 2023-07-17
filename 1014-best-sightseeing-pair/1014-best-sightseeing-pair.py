class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = [i for i in range(len(values))]
        ans = -inf
        for i in range(1,len(values)):
            if values[dp[i]] < values[dp[i - 1]] - (i - dp[i - 1]):
                dp[i] = dp[i - 1]
            ans = max(ans,values[i] + values[dp[i - 1]] - (i - dp[i - 1]))
        return ans
            
     