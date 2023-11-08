class Solution:
    def minimumSeconds(self, mat: List[List[str]]) -> int:
        
        
        que = deque()
        visited = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == "*":
                    que.append((i,j))
                    visited.add((i,j))
                if mat[i][j] == "D":
                    dest = (i,j)
                
                if mat[i][j] == "S":
                    start = (i,j)
        que.append(start)
        visited.add(start)
        level = 0
        while que:
            size = len(que)
            
            for i in range(size):
                row , col = que.popleft()
                if (row,col) == dest:
                    return level
                for x,y in [[0,1],[1,0],[-1,0],[0,-1]]:
                    newx = x + row
                    newy = col + y
                    
                    if 0 <= newx < len(mat) and 0 <= newy < len(mat[0]) and (newx,newy) not in visited and mat[newx][newy]!=  "X":
                        if mat[row][col] == "*" and mat[newx][newy] == ".":
                            mat[newx][newy] = "*"
                            que.append((newx,newy))
                            visited.add((newx,newy))
                        if mat[row][col] == "S" and mat[newx][newy] != "*":
                            mat[newx][newy] = "S"
                            que.append((newx,newy))
                            visited.add((newx,newy))
            level += 1
            
        return -1
                        
        