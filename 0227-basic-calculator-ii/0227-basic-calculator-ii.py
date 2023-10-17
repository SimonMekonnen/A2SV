class Solution:
    def calculate(self, s: str) -> int:
        
        
        stk = []
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            cur = ""
            while i < len(s) and s[i] in "0123456789":
                cur += s[i]
                i += 1
            if stk and stk[-1] == "*":
                c = stk.pop()
                stk[-1] = str(int(stk[-1]) * int(cur))
            elif stk and stk[-1] == "/":
                stk.pop()
                stk[-1] = str(int(stk[-1]) // int(cur))
            
            else:
                if not cur:
                    cur = s[i]
                    i+=1
                stk.append(cur)
        ans = int(stk[0])
        for i in range(2,len(stk),2):
            if stk[i - 1] == "-":
                ans -= int(stk[i])
            else:
                ans += int(stk[i])
        return ans