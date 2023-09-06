class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        thepop = 0
        stk = []
        for i in range(len(num)):
                while stk and thepop < k and num[i] < stk[-1]:
                    stk.pop()
                    thepop += 1
                stk.append(num[i])
            
        while stk and thepop < k:
            stk.pop()
            thepop += 1
        
        ans = ""
        for i in range(len(stk)):
            if stk[i] != "0":
                break         
        new = stk[i : ]
        return "0" if not new else ("".join(new))
        
        