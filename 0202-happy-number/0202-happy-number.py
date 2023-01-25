class Solution:
    def isHappy(self, n: int) -> bool:
        
        l = set()
        
        while n!=1:
            
            c = str(n)
            b = sum(list(map(lambda x : (int(x)**2),c)))
    
            n = b
            if b in l:
                
                return False
            
            l.add(b)
    
        return True

    