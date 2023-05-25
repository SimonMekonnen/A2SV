class Solution:
    def maxSatisfaction(self, s: List[int]) -> int:
        s.sort()
        ans  = 0

        for i in range(len(s)):
            ans += s[i] * (i + 1)
        for i in range(len(s)):
            k = i
            candidate = 0
            for j in range(i + 1,len(s)):
                candidate += s[j] * (j - k)
            ans = max(ans,candidate)
        return max(0,ans)
                
        
        
        