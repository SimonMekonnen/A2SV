class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = set(["a","e","i","o","u"])
        left,right,vcount,ans = 0,0,0,0
        for right in range(k):
            if s[right] in vow:
                vcount+=1
                ans = max(ans,vcount)
        right+=1
        while right< len(s):
            vcount+=s[right] in vow
            vcount-=s[left] in vow
            right+=1
            left+=1
            ans = max(ans,vcount)
        return ans
    
            
        
        