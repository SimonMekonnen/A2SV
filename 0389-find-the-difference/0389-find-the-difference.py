class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = Counter(s)
        t = Counter(t)
        for i in t:
            if t[i]!=c[i] or i not in c:
                return i
        