class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        seen = set()
        inbound = lambda x,y : 0 <= x < len(grid) and 0 <= y < len(grid[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        def bfs(x,y):
            que = deque([[x,y]])
            visited = set()
            visited.add((x,y))
            seen.add((x,y))
            while que:
                x,y = que.popleft()
                for dx,dy in dirs:
                    newx = x + dx
                    newy = y + dy
        
                    if inbound(newx,newy) and ((newx,newy) not in visited) and \
                    (grid[newx][newy] == 1) and ((newx,newy) not in seen):
                        que.append([newx,newy])
                        visited.add((newx,newy))
                        seen.add((newx,newy))
            return visited
        arr = []
     
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in seen and grid[row][col] == 1:
                    arr.append(bfs(row,col))
    
        ans = float("inf")
        for x,y in arr[0]:
            for X,Y in arr[1]:
                ans = min(abs(x - X) + abs(y - Y),ans)
                if ans == 2:
                    break
        return  ans - 1
                    
        
        