class Solution:
    def countHomogenous(self, s: str) -> int:
        
        left = 0
        ans = 0
        for right in range(len(s)):
            if s[right] != s[left]:
                ans += ((right - left) * (right - left + 1) / 2)
                left = right 
        ans += ((right - left + 1) * (right - left + 2) / 2)
        
        return int(ans) % (10**9 + 7)
           
    