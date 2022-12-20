class Solution:
    def maxScore(self, c: List[int], k: int) -> int:
        left = 0
        right = len(c) - 1 - k
        ans = 0
        for i in range(right + 1,len(c)):
            ans += c[i]
        right+=1
        b = ans
        while right < len(c):
            b = b+c[left]-c[right]
            ans = max(ans,b)
            left+=1
            right+=1
        return ans
        
            
            
   