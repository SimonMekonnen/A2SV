class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        pre = [0] * 52
        for i in ranges:
            pre[i[0]]+=1
            pre[i[1]+1]-=1
        for i in range(1,len(pre)):
            pre[i] = pre[i]+pre[i-1]
        while left <= right:
            if pre[left] ==0:
                return False
            left+=1
        return True
            
            
        
                
                
        