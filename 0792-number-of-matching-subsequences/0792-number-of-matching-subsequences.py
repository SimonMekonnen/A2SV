class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        dp = [[-1 for i in range(26)] for i in range(len(s))]
        
        for i in range(len(s) - 1,-1,-1):
            if i != len(s) - 1:
                dp[i] = dp[i + 1].copy()
            dp[i][ord(s[i]) - ord('a')] = i
        ans = 0
        for i in range(len(words)):
            word = words[i]
            idx = 0
            pos = 1
            for j in range(len(word)):
                char = ord(word[j]) - ord('a')
                if idx >= len(s):
                    pos = 0
                    break
                if dp[idx][char] == -1:
                    pos = 0
                    break
                idx = dp[idx][char] + 1
            if pos:
                ans += 1
        return ans
                
                
                