class Solution:
    def equalSubstring(self, s: str, t: str, m: int) -> int:
        
        left = 0
        cost = 0
        ans = 0
        for right in range(len(s)):
            cost += abs(ord(s[right]) - ord(t[right]))
            while cost > m:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            ans = max(right - left + 1,ans)
        
        return ans
        