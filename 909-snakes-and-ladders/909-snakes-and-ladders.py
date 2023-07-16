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
        que.append([1,0,0])
        level = 0
        visited = set()
        visited.add((1,0,0))
        res = inf
        while que:
               
                val,lad,ans = que.popleft()
                row = dic[val][0]
                col = dic[val][1]
                if val == n * n:
                    res = min(ans,res)
                if board[row][col] == -1 or lad == 1:
                    neigh = dire(val)
                    for x in range(neigh[0],neigh[1] + 1):
                        if (x,0,ans + 1) not in visited:
                            if ans <= n ** 2:
                                que.append([x,0,ans + 1])
                                visited.add((x,0,ans + 1))
                else:
                    if (board[row][col] ,1,ans) not in visited:
                        if ans <= n:
                            que.append([board[row][col],1,ans])
                            visited.add((board[row][col],1,ans))
        
        return res if res != inf else -1
                    
                
            