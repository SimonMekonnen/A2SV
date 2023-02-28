class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stk = [0]
        
        for i in s:
            if i == "(":
                stk.append(0)
            if i == ")":
                c = stk.pop()
                if c == 0:
                    stk[-1] += 1
                else:
                    stk[-1] += 2 * c
        return sum(stk)
   
