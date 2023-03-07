class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def valid(tc,ts):
            for i in tc:
                if i not in ts or ts[i] < tc[i]:
                    return False
            return True
        tc = Counter(t)
        left = 0
        ts = defaultdict(int)
        l= 0
        r = 0
        ans = len(s)+1
        for right in range(len(s)):
            ts[s[right]]+=1
            while valid(tc,ts) == True:
                if ans > right - left + 1:
                    ans = right - left + 1
                    l = left
                    r = right
                ts[s[left]]-=1
                left+=1
        return s[l:r+1] if ans != len(s)+1 else ""

        