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
                for i in dire:
               
                
                    if (0 <= now[0] + i[0] < len(grid)) and (0 <= now[1] + i[1] < len(grid)) and (grid[now[0] + i[0]][now[1] + i[1]] == 0) and ((now[0] + i[0],now[1] + i[1]) not in visited) :
                        que.append((now[0] + i[0],now[1] + i[1]))
                        visited.add((now[0] + i[0],now[1] + i[1]))
                        
            time += 1

        return -1
                        
                        
                    
    
       