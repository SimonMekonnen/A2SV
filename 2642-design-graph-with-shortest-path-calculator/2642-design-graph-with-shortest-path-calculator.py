class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for i in range(n)]
        self.dp = [[inf] * n for i in range(n)]
        self.t = n
        for i in range(n):
            self.dp[i][i] = 0

        for x,y,w in edges:
            self.graph[x].append((y,w))
            self.dp[x][y] = w
        for i in range(n):
            
            for row in range(n):
                for col in range(n):
                    self.dp[row][col] = min(self.dp[row][col],self.dp[row][i] + self.dp[i][col])
        
        

    def addEdge(self, edge: List[int]) -> None:
        
        x,y,w = edge
        if self.dp[x][y] > w:
            self.dp[x][y] = min(self.dp[x][y],w)
            for i in [x,y]:
                for row in range(self.t):
                        for col in range(self.t):
                            self.dp[row][col] = min(self.dp[row][col],self.dp[row][i] + self.dp[i][col])

    

    def shortestPath(self, node1: int, node2: int) -> int:
        
        return self.dp[node1][node2] if self.dp[node1][node2] != inf else -1
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)