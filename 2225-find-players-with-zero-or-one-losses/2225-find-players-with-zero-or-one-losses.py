class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        ans = [[],[]]
        s = max(matches,key = lambda x:max(x))
        count = [0] * (max(s) + 1)
        
        c = set()
        
        for i in range(len(matches)):
            count[matches[i][1]] += 1
            c.add(matches[i][0])
            c.add(matches[i][1])
            
        for i in range(1,len(count)):
            if i in c and count[i] == 0:
                ans[0].append(i)
                
            if i in c and count[i] == 1:
                ans[1].append(i)
        
        return ans
        
        
        