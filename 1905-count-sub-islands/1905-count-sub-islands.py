class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = {(0,1),(1,0),(0,-1),(-1,0)}
        visited = set()
        def dfs(x,y):
            stk = [(x,y)]
            visited.add((x,y))
            flag = True
            while stk:
                x,y = stk.pop()
                for X,Y in directions:
                    newx = X + x
                    newy = Y + y
                    if 0 <= newx < len(grid1) and 0 <= newy < len(grid1[0]):
                    
                        if grid2[newx][newy] == 1 and (newx,newy) not in visited:
                            if grid1[newx][newy] == 0:
                                flag = False
                            stk.append((newx,newy))
                            visited.add((newx,newy))
            return flag
        
        count = 0   
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] == 1 and grid1[row][col] == 1 and (row,col) not in visited and dfs(row,col):
                    count += 1
                    
   
        return count
            
                            
            
        
        