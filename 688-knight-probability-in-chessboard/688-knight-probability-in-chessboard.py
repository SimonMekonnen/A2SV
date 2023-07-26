class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        dp = [[ 0 for i in range(n)] for i in range(n)]
        
        dire = [(2,1),(1,2),(2,-1),(-1,2),(-2,1),(1,-2),(-2,-1),(-1,-2)]
        out = 0
        dp[row][column] = 1
        c = k
        mystart = deque([(row,column)])
        while k > 0:
            size = len(mystart)
            for i in range(size):
                    row,col = mystart.popleft()
                    if dp[row][col] >= 1:
                        for x,y in dire:
                            newx = row + x
                            newy = col + y
                            if 0 <= newx < n and 0 <= newy < n:
                                dp[newx][newy] += dp[row][col]
                                mystart.append((newx,newy))
                    dp[row][col] = 0
            k -=1
        mysum = 0
        for row in range(n):
            mysum += sum(dp[row])
        
        return mysum / (8**c)
            
            
        