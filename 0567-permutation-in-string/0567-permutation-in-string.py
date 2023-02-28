class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def check(s1Count,s2Count):
            for i in s1Count:
                if s1Count[i] != s2Count[i]:
                    return False
            return True
        s1c = Counter(s1)
        s2c = defaultdict(int)
        n = len(s1)
        right = n
        left = 0
        if n > len(s2):
            return False
        for i in range(n):
            s2c[s2[i]]+=1
        while right <= len(s2):
            b = check(s1c,s2c)
            if b == True:
                return True
            else:
                if right == len(s2):
                    break
                s2c[s2[right]]+=1
                s2c[s2[left]]-=1
                right+=1
                left+=1
        return False
# time complexity O(26 * n) -> O(n)
# space complexity O(26) -> O(1)
