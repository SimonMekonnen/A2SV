class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        
        stk = []
        
        for i in range(len(s)):
            if s[i] == "(":
                stk.append(i)
            if s[i] == ")":
                if stk:
                    stk.pop()
                else:
                    s[i] = ""
        for i in stk:
            s[i] = ""
        
        return "".join(s)
        
        
            