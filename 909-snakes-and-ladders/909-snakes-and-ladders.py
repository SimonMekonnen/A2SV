class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        mat = [[0 for i in range(len(board))] for i in range(len(board))]
        mynum = 1
        n = len(board)
        for row in range(len(board) - 1,-1,-1):
            for col in range(len(board)):
                mat[row][col] = mynum
                mynum += 1
            if (n - 1 - row) % 2 == 1:
                mat[row].reverse()
        dic = {}
        for row in range(n):
            for col in range(n):
                dic[mat[row][col]] = (row,col)
                
        
        def dire(k):
            nonlocal n
            return [k + 1,min(k + 6,n**2)]
        
        que = deque()
        que.append(1)
        level = 0
        visited = set()
        visited.add(1)
        while que:
            size = len(que)
            for i in range(size):
                cur = que.popleft()
                if cur == n * n:
                    return level
                for i in range(1,7):
                    if cur + i <= n**2:
                        neigh = dic[cur + i]
                        row = neigh[0]
                        col = neigh[1]
                        if board[row][col] == -1:
                            if cur + i not in visited:
                                que.append(cur + i)
                                visited.add(cur + i)
                        else:
                            if board[row][col] not in visited:
                                que.append(board[row][col])
                                visited.add(board[row][col])
            level += 1
        return -1
                
                        
            