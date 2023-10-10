class Solution:
    def subStrHash(self, s: str, power: int, m: int, k: int, hashu: int) -> str:
        myhash = 0
        left = len(s) - 1
        p = k
        l = 0
        r = 0
        for right in range(len(s) - 1,-1,-1):
            if p - 1 >= 0:
                myhash += (ord(s[right]) - ord('a') + 1) * pow(power, p - 1,m)
                p -= 1
                myhash %= m
            else:
                if myhash % m== hashu:
                    l = right + 1
                    r = left + 1
                myhash -= (ord(s[left]) - ord('a') + 1) * pow(power,k - 1,m)
                myhash *= power
                myhash += (ord(s[right]) - ord('a') + 1)
                left -= 1
                myhash %= m
        if myhash % m == hashu:
            return s[right : left + 1]
        return s[l : r]