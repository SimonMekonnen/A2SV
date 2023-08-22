class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        up  = {1 : [], 2 : [2,3,4],3 : [],4 : [],5 : [3,4,2],6 : [4,3,2]}
        down = {1  : [],2 : [2,6,5],3 : [5,6,2] , 4 : [6,5,2],5 : [],6 : []}
        left = {1 : [1,4,6],2 : [], 3 : [1,4,6] , 4 : [],5 : [6,4,1] , 6 : []}
        right = {1 : [1,3,5],2 : [], 3 : [],4 : [5,3,1],5 : [],6 : [3,5,1]}
        que = deque([])
        que.append([0,0])
        pos = 0
        while que:
            row,col = que.popleft()
            if grid[row][col] == -1:
                continue
            if row == len(grid) - 1  and col == len(grid[0]) - 1:
                pos = 1
            v = grid[row][col]
            grid[row][col] = -1
            for x,y in [[1,0],[0,1],[-1,0],[0,-1]]:
                newx = x + row
                newy = y + col
                if y == 1:
                    tofound = right[v]
                if y == -1:
                    tofound = left[v]
                if x == 1:
                    tofound = down[v]
                if x == -1:
                    tofound = up[v]
                    
                if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and grid[newx][newy] in tofound:
                    que.append([newx,newy])
    
        
        if pos:
            return True
            