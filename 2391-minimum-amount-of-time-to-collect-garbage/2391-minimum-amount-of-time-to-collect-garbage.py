class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
            m,g,p = 0,0,0
            total  = 0
            pre = [0]
            for i in travel:
                pre.append(pre[-1] + i)
            for i,n in enumerate(garbage):
                total += len(garbage[i])
                if "P" in n:
                    total+=pre[i] - pre[p]
                    p = i
                if "M" in n:
                    total+=pre[i] - pre[m]
                    m = i
                if "G" in n:
                    total+=pre[i] - pre[g]
                    g = i
            return total
        