class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        b = Counter(arr)
        c = list(b.values())
        c.sort()
        for i in range(1,len(c) ):
            if c[i] == c[i-1]:
                return False
        return True
        