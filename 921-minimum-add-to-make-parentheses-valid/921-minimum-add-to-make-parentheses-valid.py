class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        close = 0
        for i in s:
            if i=="(":
                stk.append(i)
            elif stk and i == ")":
                stk.pop()
            elif not stk and i == ")":
                close+=1
        return len(stk) + close
        