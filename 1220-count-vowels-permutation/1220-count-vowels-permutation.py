class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        data = {'a' : 0,'e' : 1, 'i' : 2, "o" : 3 , 'u' : 4}
        another = {0 : 'a',1 : "e", 2 : "i", 3 : "o" , 4 : "u"}
        which =  {'a' : "e",'e' : "ai", 'i' : "aeou", "o" : "iu" , 'u' : "a"}
        
        dp = [[0 for i in range(5)] for i in range(n)]
        for i in range(5):
            dp[0][i] = 1
    
        for i in range(n - 1):
            for j in range(5):
                cur = dp[i][j]
                for k in which[another[j]]:
                    dp[i + 1][data[k]] += cur
    
        return sum(dp[-1]) % (10 ** 9 + 7)
            