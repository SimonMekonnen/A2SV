class Solution:
    def numTrees(self, n: int) -> int:
        dp =  [0 for i in range(n + 1)]
        if n == 1 or n == 2:
            return n
        dp[1] =  1
        dp[2] = 2
        dp[0] = 1
        
        for i in range(3,n + 1):
            cur = 0
            
            for j in range(1,i + 1):
                left = j - 1
                right = i - j
                cur += dp[left] * dp[right]
            dp[i] = cur

        return dp[-1]       
    