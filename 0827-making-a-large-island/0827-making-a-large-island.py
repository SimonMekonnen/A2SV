class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        
        visited = [[0] * len(grid) for i in range(len(grid))]
        dic = defaultdict(int)
        def bfs(row,col,id):
            cur = set()
            que = deque([[row,col]])
         
            while que:
                row,col = que.popleft()
                if (row,col) in cur:
                    continue
                cur.add((row,col))
                for x,y in [[0,1],[1,0],[-1,0],[0,-1]]:
                    newcol = y + col
                    newrow = x + row
                    if 0 <= newcol < len(grid) and 0 <= newrow < len(grid) and grid[newrow][newcol] == 1:
                        
                        que.append([newrow,newcol])

            for x,y in cur:
                visited[x][y] = id
            dic[id] = len(cur)
        id = 1
        for row in range(len(grid)):
            for col in range(len(grid)):
                if visited[row][col] == 0 and grid[row][col] == 1:
                    bfs(row,col,id)
                    id += 1
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col] == 0:
                    cur = set()
                    for x,y in [[0,1],[1,0],[-1,0],[0,-1]]:
                        newcol = y + col
                        newrow = x + row
                        if 0 <= newcol < len(grid) and 0 <= newrow < len(grid) and grid[newrow][newcol] == 1:
                            cur.add(visited[newrow][newcol])
                    t = 0
                    for i in cur:
                        t += dic[i]
                    ans = max(t + 1,ans)
                else:
                    ans = max(ans,dic[visited[row][col]])
     
        return ans