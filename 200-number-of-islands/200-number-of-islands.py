class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def dfs(row,col):
            if (row,col) in visited:
                return 
            visited.add((row,col))
            for x,y in [[1,0],[0,1],[-1,0],[0,-1]]:
                newx = x + row
                newy = y + col
                if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]):
                    if grid[newx][newy] == "1":
                        dfs(newx,newy)
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])): 
                if (row,col) not in visited and grid[row][col] == "1":
                    dfs(row,col)
                    count += 1
        return count
        
    
        