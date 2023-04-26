class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        
        for i in range(len(redEdges)):
            red[redEdges[i][0]].append(redEdges[i][1])
        for i in range(len(blueEdges)):
            blue[blueEdges[i][0]].append(blueEdges[i][1])
        
        que = deque([[0,0],[0,1]])
        visited = set()
        another = set()
        time = 0
        while que:
            s = len(que)
         
            for _ in range(len(que)):
                now = que.popleft()
                visited.add((now[0],time))
                another.add((now[0],now[1]))
                if now[1] == 0:
                    for i in blue[now[0]]:
                        if (i,1) not in another:
                            que.append([i,1])
                else:
                    for i in red[now[0]]:
                        if (i,0) not in another:
                            que.append([i,0])
                    
            
            time += 1
        ans = [-1 for i in range(n)]
        for i in visited:
            if ans[i[0]] != -1:
                ans[i[0]] = min(ans[i[0]],i[1])
            else:
                ans[i[0]] = i[1]
                
        return ans