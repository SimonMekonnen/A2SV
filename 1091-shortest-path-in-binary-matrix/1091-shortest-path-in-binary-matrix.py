class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dire = [[-1,0],[0,-1],[1,0],[0,1],
                [1,1],[-1,-1],[-1,1],[1,-1]]
        if grid[0][0] == 1:
            return  -1
        que = deque([(0,0)])
        visited = set()
        time = 0
        while que:
            size = len(que)
            for _ in range(size):
                
                now = que.popleft()
                
                if (len(grid) - 1 , len(grid) - 1) == now:
                    return time + 1
                for x,y in dire:
                    
                    newx = now[0] + x
                    newy = now[1] + y
                    
                    if (0 <= newx  < len(grid)) and (0 <= newy < len(grid)) and (grid[newx][newy] == 0) and ((newx,newy) not in visited) :
                        que.append((newx,newy))
                        visited.add((newx,newy))
                        
            time += 1

        return -1
                        
                        
                    
    
       