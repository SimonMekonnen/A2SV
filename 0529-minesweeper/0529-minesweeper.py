class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        cx,cy = click[0],click[1]
        if board[cx][cy] == "M":
            board[cx][cy] = "X"
            return board
        
        dirs = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        
        visited = set()
        visited.add((cx,cy))
        n,m = len(board),len(board[0])
        inbound = lambda x,y: 0 <= x < n and 0 <= y < m
        
        def countMines(cx,cy):
            count = 0
          
            for x,y in dirs:
                newx , newy = x + cx, y + cy
                
                if inbound(newx,newy) and board[newx][newy] == "M":
                    count += 1
                    
            return count
        
        def dfs(cx,cy):
            count  = countMines(cx,cy)
            if count:
                board[cx][cy] = str(count)
                return 
        
            board[cx][cy] = "B"
            for x,y in dirs:
                newx = x + cx
                newy = y + cy
                if inbound(newx,newy) and board[newx][newy] == "E":
                    dfs(newx,newy)
            
        dfs(cx,cy)
        return board
                    
            
            
        