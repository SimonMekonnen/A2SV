class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        d = int(c**(1/2))
        
        right = d
        left = 0
        
        while left <= right:
            
            if right**2 + left**2 == c:
                
                return True
            elif right**2 + left**2 > c:
                right -= 1
            
            else:
                left+=1
                
        return False 
                
        