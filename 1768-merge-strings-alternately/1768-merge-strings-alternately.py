class Solution:
    def mergeAlternately(self, wo1: str, wo2: str) -> str:
        ans = ""
        l = 0
        r = 0
        for i in range((len(wo1)+ len(wo2))):
            if l < len(wo1) and i%2 == 0:
                ans+=wo1[l]
                l+=1
            elif r < len(wo2) and i%2 == 1:
                ans+=wo2[r]
                r+=1
        ans += wo1[l:] if l  < len(wo1) else ""
        ans += wo2[r:] if r < len(wo2) else ""
        return ans
                       
        
            
        