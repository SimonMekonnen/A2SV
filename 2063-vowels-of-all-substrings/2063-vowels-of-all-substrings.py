class Solution:
    def countVowels(self, word: str) -> int:
        
        vowel = set(["a",'e','i','o','u'])
        dp = 0
        if word[0] in vowel:
            dp = 1
        ans = dp
        for i in range(1,len(word)):
            if word[i] in vowel:
                dp += i + 1
            ans += dp
    
        return ans
        
        
        