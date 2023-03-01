
class Solution:
    def getRow(self, ri: int) -> List[int]:
        
        return [(math.factorial(ri)//((math.factorial(i) * math.factorial(ri - i)))) for i in range(ri + 1)]
        
        
       
        
        
    
        
        