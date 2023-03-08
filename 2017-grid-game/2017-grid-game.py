class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        for row in range(len(grid)):
            
            for col in range(1,len(grid[0])):
                
                grid[row][col] += grid[row][col - 1]
                
        ans = float('inf')
        
        for i in range(len(grid[0])):
            
            top = grid[0][-1] - grid[0][i]
            bottom = grid[1][i - 1] if i != 0 else 0
            
            ans =min(ans, max(top,bottom))
        
        return ans
            
            