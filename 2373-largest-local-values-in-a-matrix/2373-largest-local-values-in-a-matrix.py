class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        ans = [[0 for i in range(len(grid ) - 2)] for i in range(len(grid) - 2)]
        direction = [(0,1),(0,2),(0,0),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        for row in range(len(grid) - 2):
            
            for col in range(len(grid) - 2):
                max_ = grid[row][col]
           
                for i in direction:
                    max_ = max(max_,grid[row + i[0]][col + i[1]])
                
                ans[row][col] = max_
                
    
    
        return ans
        
        
        
        
       