class Solution:
    def knightDialer(self, n: int) -> int:
        
        dic = {0 : [4,6],1 : [8,6],2 : [7,9], 3 : [4,8],4 : [0,3,9],
               5 : [], 6 : [0,1,7], 7 : [2,6], 8 : [1,3], 9 : [4,2]}
        
        dp = [[0] * 10 for i in range(n)]
        for i in range(10):
            dp[0][i] = 1
        
        for i in range(len(dp) - 1):
            for j in range(10):
                for k in dic[j]:
                    dp[i + 1][k] += dp[i][j]
                    dp[i + 1][k] %= (10**9 + 7)
        return sum(dp[-1]) % (10 ** 9 + 7)              