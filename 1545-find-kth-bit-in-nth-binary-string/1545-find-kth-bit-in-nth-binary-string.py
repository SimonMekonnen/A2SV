class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        if n == 1:
            
            return "0"   
        if k  == (2 ** n // 2):
            return "1" 
        if k > 2**(n) // 2:
            return "1" if self.findKthBit(n - 1, 2**n - k) == "0" else "0"
        else:
            return self.findKthBit(n - 1,k)
        
        
        
            
        