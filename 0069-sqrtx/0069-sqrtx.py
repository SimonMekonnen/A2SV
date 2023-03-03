class Solution:
    def mySqrt(self, x: int) -> int:
        
        arr = []
        
        for i in range(50000):
            arr.append(i*i)
        
        for i in range(0,len(arr)):
            if arr[i] == x:
                return i
            elif arr[i] > x:
                return i - 1
            
        
  
        
        