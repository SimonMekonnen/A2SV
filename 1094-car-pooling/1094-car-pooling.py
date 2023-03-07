class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        pre = [0] * 1002
        
        for p,f,t in trips:
            
            pre[f] += p
            pre[t] -= p
    
        for i in range(0,len(pre)):
            
            if i != 0 : pre[i] += pre[i - 1]
            if pre[i] > capacity:
                return False
        return True
        
        
        
            
        
       
            
        