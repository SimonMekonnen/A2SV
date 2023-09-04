class Solution:
    def wordBreak(self, s: str, dic: List[str]) -> bool:
        dic = set(dic)
        dp = [i for i in range(len(s) + 1)]
        for i in range(1,len(s) + 1):
            for j in range(i):
                if s[j:i] in dic:
                    dp[i] = min(dp[i],dp[j])
                else:
                    dp[i] = min(dp[i - 1] + 1,dp[i])
        return dp[-1] == 0
        