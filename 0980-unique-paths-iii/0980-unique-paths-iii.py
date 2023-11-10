class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
      
        ans = 0
        count =  0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row = i
                    col = j
                elif grid[i][j] == 2:
                    endr = i
                    endc = j
                elif grid[i][j] == -1:
                    count += 1
     
        target =  len(grid) * len(grid[0]) - count
                    
        ans = 0
        def bt(row,col,visited):
            nonlocal ans
            if len(visited) == target and visited[-1]  == (endr,endc):
                ans += 1
                return 
    
            for x,y in [[1,0],[0,1],[-1,0],[0,-1]]:
                newx = x + row
                newy = y + col
                
                if  0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and grid[newx][newy] != -1 and (newx,newy) not in visited:
                    visited.append((newx,newy))
                    bt(newx,newy,visited)
                    visited.pop()
                    
          
        bt(row,col,[(row,col)])
        
        return ans