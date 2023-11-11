class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        index = [ i for i in range(len(plantTime))]
        index.sort(key = lambda x : growTime[x],reverse = True)
                 
        ans = 0
        curtime = 0     
        for i in range(len(index)):
            curtime += plantTime[index[i]]
            ans = max(curtime + growTime[index[i]],ans)
        
        return ans