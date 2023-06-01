class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        dp = [0 for i in range(len(questions))]
        dp[-1] = questions[-1][0]
        
        for i in range(len(questions) - 1 - 1,-1,-1):
            
            toadd = dp[i + questions[i][1] + 1] if i + questions[i][1] + 1 < len(questions) else 0
            dp[i] = max(questions[i][0] + toadd,dp[i + 1])
            
        return max(dp)
        