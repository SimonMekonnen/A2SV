class Solution:
    def romanToInt(self, s: str) -> int:
        maap = {
            "I": 1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
        }
        
        
        i = 0
        ans = 0
        while i < len(s):
            if i != len(s) - 1 and maap[s[i]] < maap[s[i + 1]]:
                ans += maap[s[i : i + 2]]
                i += 2
            else:
                ans += maap[s[i]]
                i += 1
        return ans
                

    
    
        