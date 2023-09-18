class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0] * (len(text2) + 1) for i in range(len(text1) + 1) ]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j],dp[i][j - 1])
        ans = ""
        row = len(text1)
        col = len(text2)
        while dp[row][col] != 0:
            if text1[row - 1] == text2[col - 1]:
                ans += text1[row - 1]
                row -= 1
                col -= 1
            else:
                if dp[row - 1][col] > dp[row][col - 1]:
                    row -= 1
                else:
                    col -= 1
        return dp[-1][-1]
        
        