class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        c = Counter(deck)
        now = min(c.values())
        factors = []
        p = True
        for i in c:
            if c[i] % now != 0 or len(deck) == 1 or now == 1:
                p = False
        if p:
            return True
        for i in range(2,now):
            if now % i == 0:
                factors.append(i)
        for i in factors:
            flag = True
            for j in c:
                if (c[j] % i) != 0:
                    flag = False
            if flag:
                return True
        return False
                