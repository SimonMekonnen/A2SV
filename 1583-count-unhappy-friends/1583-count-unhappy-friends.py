class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        
        mat = [[-1 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n - 1):
                mat[i][preferences[i][j]] = j
        un = set()
        for i in range(len(pairs)):
            x,y = pairs[i]
            for j in range(len(pairs)):
                if i != j:
                    u,v = pairs[j]
                    if (mat[x][y] > mat[x][u] and mat[u][v] > mat[u][x]) or\
                    (mat[x][y] > mat[x][v] and mat[v][u] > mat[v][x]):
                        un.add(x)
                        
                    if (mat[y][x] > mat[y][u] and mat[u][v] > mat[u][y]) or\
                    (mat[y][x] > mat[y][v] and mat[v][u] > mat[v][y]):
                        un.add(y)
                    
        return len(un)
                    
                    
                