class Solution:
    def numTeams(self, ratings: List[int]) -> int:
        
        
        dp = [0 for i in range(len(ratings))]
        ans = 0
        for i in range(len(dp)):
            for j in range(i):
                if ratings[i] > ratings[j]:
                    ans += dp[j]
                    dp[i] += 1
        dp = [0 for i in range(len(ratings))]
        for i in range(len(dp)):
            for j in range(i):
                if ratings[i] < ratings[j]:
                    ans += dp[j]
                    dp[i] += 1
        return ans