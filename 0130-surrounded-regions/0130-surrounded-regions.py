class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        n = len(board)
        m = len(board[0])
        
        inbound = lambda x, y : 0 <= x < n and 0 <= y < m
        boarder = lambda x, y : x == 0 or x == n - 1 or y == 0 or y == m - 1
        visited = set()
        
        def dfs(x,y):
            visited.add((x,y))
            for dx,dy in dirs:
                newx = x + dx
                newy = y + dy
                if inbound(newx,newy) and (newx,newy) not in visited and board[newx][newy] == "O":
                    dfs(newx,newy)
        
        for row in range(n):
            for col in range(m):
                if (row,col) not in visited and \
                  boarder(row,col) and board[row][col] == "O":
                                dfs(row,col)
        for row in range(n):
            for col in range(m):
                if (row,col) not in visited:
                    board[row][col] = "X"
        
        return board
                                
                                
                    
        
        
        
                    
        
                
        