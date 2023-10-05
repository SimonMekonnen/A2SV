class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        
        stk = []
        for i in s:
            if stk and stk[-1][0] == i:
                if stk[-1][1] + 1 == k:
                    stk.pop()
                else:
                    stk[-1][1] += 1
            else:
                stk.append([i,1])
        ans = ""
        for i,k in stk:
            ans += i * k
        return ans