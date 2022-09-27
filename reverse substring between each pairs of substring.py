class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        stk2 = []
        i = 0
        while i < len(s):
            if s[i] == ")":
                while stk[-1] != "(":
                    b = stk.pop()
                    stk2.append(b)
                stk.pop()
                stk+=stk2
                stk2 = []
                i+=1
            else:
                stk.append(s[i])
                i+=1
        return "".join(stk)
    
                

        