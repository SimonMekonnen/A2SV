class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        o = 0
        c = 0
        ans = 0
        s = list(s)
        
        for i in range(len(s)):
            
            if s[i] == ")":
                c+= 1
            if s[i] == "(":
                o += 1
            
            if c > o:
                s[i] = ""
                c-=1 
        
        now = o - c
        if now > 0:
            for i in range(len(s ) - 1, -1 ,-1):
                if s[i] == "(":
                    s[i] = ""
                    now -= 1
                if now == 0:
                    break
        return "".join(s)
        
        
            