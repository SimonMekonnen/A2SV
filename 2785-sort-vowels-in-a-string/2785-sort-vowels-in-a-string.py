class Solution:
    def sortVowels(self, s: str) -> str:
        
        
        v = []
        vowels = "AEIOUaeiou"
        
        for i in s:
            if i in vowels:
                v.append(i)
        
        v.sort()
        p = 0
        ans = ""
        
        for i in s:
            if i in vowels:
                ans += v[p]
                p += 1
            else:
                ans += i
        return ans
        
        
        
        
                