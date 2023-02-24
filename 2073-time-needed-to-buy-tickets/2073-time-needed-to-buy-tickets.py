class Solution:
    def timeRequiredToBuy(self, t: List[int], k: int) -> int:
        ans = 0
        b = len(t)
        i = 0
        while t[k] > 0:
            i = i % b
            if t[i] > 0:
                ans += 1
            t[i] -= 1
            i += 1
        
        return ans 

            
        