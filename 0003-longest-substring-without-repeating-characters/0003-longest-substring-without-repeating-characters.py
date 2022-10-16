class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans =  0
        chars = {}
        
        for right in range(len(s)):
            if s[right] in chars and left <= chars[s[right]]:
                left = chars[s[right]]+1
            else:
                ans = max(right - left + 1 , ans)
            chars[s[right]] = right
                
    
        return ans
    
      
    