class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        
        
        
        dic = set()
        
        before = set()
        
        
        ans = set()
        
        for i in range(len(s)):
            cur = s[i]
            
            for j in range(26):
                if cur + (chr(ord('a') + j)) in dic:
                    ans.add(cur + cur + (chr(ord('a') + j)) + cur )
            
            for j in before:
                dic.add(j + cur)
            before.add(s[i])
            
        return len(ans)