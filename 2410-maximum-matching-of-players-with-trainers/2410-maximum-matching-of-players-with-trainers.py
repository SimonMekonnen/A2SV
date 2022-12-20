class Solution:
    def matchPlayersAndTrainers(self, p: List[int], t: List[int]) -> int:
        p.sort()
        t.sort()
        i = 0
        j = 0
        count = 0
        while i < len(p) and j < len(t):
            if t[j] >= p[i]:
                j+=1
                i+=1
                count+=1
            else:
                j+=1
        return count