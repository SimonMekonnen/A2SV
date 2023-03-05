class Solution:
    def decodeString(self, s: str) -> str:
        
        ans = ""
        i = 0
        while i < len(s):
            if s[i] == "[":
                b = 1
                j = i + 1
                while b != 0:
                    if s[j] == "[":
                        b += 1
                    elif s[j] == "]":
                        b -= 1
                    j += 1
                    
                n = i - 1
                while n >= 0 and s[n].isdigit():
                    n -= 1
 
                ans += self.decodeString(s[i + 1 : j - 1]) * int(s[n + 1 : i])
                i = j-1
            elif not s[i].isdigit():
                ans += s[i]
            i += 1
        
        return ans
            
        
        
        