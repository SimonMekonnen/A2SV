class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        que = deque()
        visited = set()
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    que.append((row,col))
                    visited.add((row,col))
        
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        count = 0
        while que:
            size = len(que)
            for _ in range(size):
                x,y = que.popleft()
                mat[x][y] = count
                for X,Y in direction:
                    newx = X + x
                    newy = Y + y
                    if 0 <= newx < len(mat) and 0 <= newy < len(mat[0]) and (newx,newy) not in visited:
                        que.append((newx,newy))
                        visited.add((newx,newy))
                
                
                
            count += 1
        
        return mat
                

        