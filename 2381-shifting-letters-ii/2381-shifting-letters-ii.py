class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre = [0] * (len(s)+1)
        for i,j,k in shifts:
            if k == 0:
                pre[i]-=1
                pre[j+1]+=1
            if k == 1:
                pre[i]+=1
                pre[j+1]-=1
        pre.pop()
        s = list(s)
        total = 0
        for i in range(len(s)):
            total += pre[i]
            some = (ord(s[i]) - ord("a")) + total
            s[i] = chr(ord("a") + some%26)
        return "".join(s)
            
            