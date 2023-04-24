class Solution:
    def groupThePeople(self, gs: List[int]) -> List[List[int]]:
        
        table = defaultdict(list)
        ans = []
        for i in range(len(gs)):
            
            if len(table[gs[i]]) == gs[i]:
                ans.append(table[gs[i]])
                table[gs[i]] = []
            table[gs[i]].append(i)
            
        for i in table:
            if len(table[i]) != 0:
                ans.append(table[i])
                
        return ans
        
       
                
     