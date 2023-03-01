class Solution:
    def getRow(self, ri: int) -> List[int]:
        
        if ri == 0:
            return [1]
        
        arr = [1,1]
        ar = 2
        while ri > 1:
            new = [1]
            for i in range(len(arr) - 1):
                new.append(arr[i] + arr[i + 1])
            
            new.append(1)
            arr = [i for i in new]
            ri -= 1
            ar += 1
        
        return arr
        
        
        
    
        
        