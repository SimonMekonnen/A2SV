class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        horizontal = [max(arr) for arr in grid]
        vertical =  []
        for col in range(len(grid[0])):
            now  = grid[0][col]
            for row in range(len(grid)):
                if grid[row][col] > now:
                    now = grid[row][col]
                    
            vertical.append(now)
        ans = 0   
        for row in range(len(grid)):
            
            for col in range(len(grid)):
                
                ans+= min(horizontal[row],vertical[col]) - grid[row][col]
        
        return ans
            