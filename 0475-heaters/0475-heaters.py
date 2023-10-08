class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        ans = 0
        for i in houses:
            c = bisect_left(heaters,i)
            if c >= len(heaters):
                c -= 1
   
            d = c - 1
            e = c + 1
            g = abs(heaters[c] - i)
         
            if d >= 0:
                g = min(g,abs(heaters[d] - i))
            if e < len(heaters):
                g = min(g,abs(heaters[e] - i))
        
            ans = max(ans , g)
        return ans