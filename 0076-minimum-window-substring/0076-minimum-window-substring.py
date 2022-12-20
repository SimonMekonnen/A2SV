class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contains(sc,tc):
            for i in tc:
                if i not in sc or sc[i] < tc[i]:
                    return False
            return True
        Tcount = Counter(t)
        Scount = defaultdict(int)
        left = 0
        right = 0
        ans = math.inf
        l = 0
        r = 0
        if len(s)<len(t):
            return ""
        while right <= len(s):
            b = contains(Scount,Tcount)
            if b == False:
                if right!= len(s):
                    Scount[s[right]]+=1
                right+=1
            else:
                if right - left < ans:
                    l = left
                    r = right
                    ans = right - left
                Scount[s[left]]-=1
                left+=1
        return s[l:r]