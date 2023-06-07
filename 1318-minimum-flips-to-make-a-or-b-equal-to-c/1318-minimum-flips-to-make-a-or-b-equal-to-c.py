class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(32):
            cura = (a >> i) % 2 == 1
            curb = (b >> i) % 2 == 1
            curc = (c >> i) % 2 == 1
            if cura | curb != curc:
                if curc == 1:
                    ans += 1
                if curc == 0:
                    ans += cura + curb
        return ans
        
                    
    
        
   
        