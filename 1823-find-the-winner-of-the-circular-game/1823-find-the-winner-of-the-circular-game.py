class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        arr = [i for i in range(1,n + 1)]
        
        c = n
        i = 0
        r = 0
        while c != 1:
            if arr[i%n] != "_":
                r+=1
            if r == k:
                arr[i%n] = "_"
                r = 0
                c-=1
            i+=1
        for i in arr:
            if i!="_":
                return i
        
        
            
                
        
        
                
            
            
            
        
        
        