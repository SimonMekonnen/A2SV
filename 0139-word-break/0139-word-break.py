class Solution:
    def wordBreak(self, s: str, dic: List[str]) -> bool:
        dic = set(dic)
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        for i in range(1,len(s) + 1):
            for j in range(i):
                if s[j:i] in dic:
                    dp[i] = dp[i] or dp[j]   
        return dp[-1] == 1
        