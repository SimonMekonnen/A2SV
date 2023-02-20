class Solution:
    def po(self,x,n):
        if n == 1:
            return x
        elif n == 0:
            return 1
        if n % 2 == 0:
                b = self.po(x,n//2)
                return pow(b ,2,1000000007)
        else:
                b = self.po(x,n//2)
                return pow(b,2,1000000007) * x
         
    def countGoodNumbers(self, n: int) -> int:     
         
        c = n % 2 == 1
         
        return ((self.po(20,n//2) * (5 ** c))) % 1000000007
    
    
        
        
        