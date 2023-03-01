class Solution:
    def myPow(self, x: float, n: int) -> float:  
        if n in [0,1,-1]: return x**n
        c = self.myPow(x, n //2)
        return c * c if n%2 == 0 else c * c * x
        

            
        