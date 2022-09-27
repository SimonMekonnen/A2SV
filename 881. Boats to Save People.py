class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        p.sort()
        l = 0
        r = len(p) - 1
        ans = 0
        while l <= r:
            if p[l] + p[r] <= limit:
                ans+=1
                l+=1
                r-=1
            else:
                ans+=1
                r-=1
        return ans
            
        