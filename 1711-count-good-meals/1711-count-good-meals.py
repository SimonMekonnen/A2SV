class Solution:
    def countPairs(self, deli: List[int]) -> int:

        dic = defaultdict(int)
        ans = 0
        deli.sort()
        for j in range(len(deli)):
            i = 1
            while i < deli[j]:
                i*=2
            cu = i - deli[j]
            if cu in dic:
                ans+=dic[cu]

            if i == deli[j]:
                if i*2 - deli[j] in dic:
                    ans+=dic[i*2 - deli[j]]
            
            dic[deli[j]]+=1
        return ans % (10**9 + 7)

        