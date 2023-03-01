class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        c = self.myPow(x, n //2)
        
        return c * c if n%2 == 0 else c * c * x
        

            
        