class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = 0
        ans = -inf
        for i in range(1,len(values)):
            ans = max(ans,values[i] + values[dp] - (i - dp))
            if values[i] >= values[dp] - (i - dp):
                dp = i
            
        return ans
            
     