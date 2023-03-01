class Solution:
    def getRow(self, ri: int) -> List[int]:
        
        if ri == 0:
            return [1]
        
        else:
            b = self.getRow(ri - 1)
            c = [1]
            for i in range(len(b) - 1):
                c.append(b[i] + b[i + 1])
            c.append(1)
            
            return  c
        
        
        
    
        
        