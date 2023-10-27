class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        pos = 1
        if set(word1) != set(word2):
            pos = 0
        
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        c1 = list(count1.values())
        c2 = list(count2.values())
        c1.sort()
        c2.sort()
        if not pos:
            return False
        return c1 == c2