class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        arr = [[0 for i in range(n)] for j in range(m) ]
       
        arr[0][0] = 1
        
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    continue
                arr[row][col] += arr[row -1][col] + arr[row][col-1] 
    
        return arr[-1][-1]
                
        
        
        
        
        
        
        
       