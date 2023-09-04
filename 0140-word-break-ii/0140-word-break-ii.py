class Solution:
    def wordBreak(self, s: str, dic: List[str]) -> List[str]:
        dic = set(dic)
        dp = [i for i in range(len(s) + 1)]
        here = [[] for i in range(len(s))]
        for i in range(1,len(s) + 1):
            for j in range(i):
                if s[j:i] in dic:
                    dp[i] = min(dp[i],dp[j])
                    if dp[j] == 0:
                        here[i - 1].append(j)
                else:
                    dp[i] = min(dp[i - 1] + 1,dp[i])
        ans = []
        def bt(index,string):
            if index < 0:
                ans.append(string.strip())
                return 
            
            for i in here[index]:
                bt(i - 1,s[i:index + 1] + " " + string)
        bt(len(here) - 1,"")
        return ans
                
            
            
    