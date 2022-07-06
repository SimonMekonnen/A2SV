from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(lambda: 0)
        for i in nums:
            dic[i]+=1
        d=list(dic.items())
        d.sort(key=lambda x:x[1],reverse=True)
        b=[]
        i=0
        while k>0 and i<len(d):
            b.append(d[i][0])
            i+=1
            k-=1
        return b