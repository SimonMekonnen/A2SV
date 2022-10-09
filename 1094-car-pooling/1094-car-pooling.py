class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pre = [0] * 1001
        for pas,fro,to in trips:
            pre[fro]+=pas
            pre[to]-=pas
        total = 0
        pree = []
        for i in pre:
            total+=i
            if total > capacity:
                return False
        return True
        
        
        
            
        
       
            
        