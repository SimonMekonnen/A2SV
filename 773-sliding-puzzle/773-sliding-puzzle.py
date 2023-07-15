class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        visited = set()
        que = deque([board])
        def s(mat):
            s = ''
            for row in range(2):
                for col in range(3):
                    s += str(mat[row][col])
            return s
        def swap(mat,zrow,zcol,row,col):
            cur = [[i for i in mat[j]] for j in range(2)]
            cur[zrow][zcol],cur[row][col] = cur[row][col],cur[zrow][zcol]
            return cur
    
        dire = [(1,0),(0,1),(-1,0),(0,-1)]
        level = 0
        visited.add(s(board))
        while que:
            size = len(que)
            for i in range(size):
                cur = que.popleft()
                if s(cur) == '123450':
                    return level
                
                for row in range(2):
                    for col in range(3):
                        if cur[row][col] == 0:
                            zcol = col
                            zrow = row
                for x,y in dire:
                    row = x + zrow
                    col = y + zcol
                    if 0 <= row <= 1 and 0 <= col <= 2:
                        newmat = swap(cur,zrow,zcol,row,col)
                        if s(newmat) not in visited:
                            que.append(newmat)
                            visited.add(s(newmat))
            level += 1
        return -1
                
                            
                
                
                
        