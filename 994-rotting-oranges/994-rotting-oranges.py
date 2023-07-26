class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        que = deque()
        visited = set()
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    que.append((row,col))
                if grid[row][col] == 1 or grid[row][col] == 2:
                    count += 1
        level = 0 

        while que:
            size = len(que)
          
            for i in range(size):
                row,col = que.popleft()
                visited.add((row,col))
                for x, y in [[1,0],[0,1],[-1,0],[0,-1]]:
                    newx = row + x
                    newy = col + y
                    if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]):
                        if grid[newx][newy] == 1 and (newx,newy) not in visited:
                            que.append((newx,newy))
                            visited.add((newx,newy))
         
            level += 1
        if count == 0:
            return 0
        if count == len(visited):
            return level - 1
        else:
            return -1
                        
        
        
        