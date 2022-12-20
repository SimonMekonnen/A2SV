class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        b = Counter(arr)
        c = list(b.values())
        a = set()
        for i in c:
            if i in a:
                return False
            a.add(i)
        return True
        