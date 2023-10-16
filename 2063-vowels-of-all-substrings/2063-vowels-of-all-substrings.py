class Solution:
    def countVowels(self, word: str) -> int:
        
        vowel = set(["a",'e','i','o','u'])
        dp = [0 for i in range(len(word))]
        if word[0] in vowel:
            dp[0] = 1
        for i in range(1,len(word)):
            if word[i] in vowel:
                dp[i] += dp[i - 1] + i + 1
            else:
                dp[i] = dp[i - 1]
        return sum(dp)
        
        
        