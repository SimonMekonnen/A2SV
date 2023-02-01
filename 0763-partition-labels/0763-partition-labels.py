class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        count  = Counter(s)
        new = defaultdict(int)
        ans = []
        
        for i in s:
            new[i]+=1
            Flag = True
            for j in new:
                if new[j] != count[j]:
                    Flag = False
            if Flag:
                ans.append(sum(new.values()))
                new.clear()

        return ans
        
        
        