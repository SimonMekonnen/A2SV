class Solution:
    def calcEquation(self, eq: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        
        graph = defaultdict(set)
        for i in range(len(values)):
            graph[eq[i][0]].add((eq[i][1],values[i]))
            graph[eq[i][1]].add((eq[i][0],1/values[i]))
        
        ans = []
        for x,y in queries:
            if x == y:
                if len(graph[x]) != 0:
                    ans.append(1)
                else:
                    ans.append(-1)
            else:
                que = deque([[x,1]])
                visited = set()
                found = 0
                while que:
                    x,total = que.popleft()
                    if x == y:
                        found = 1
                        ans.append(total)
                        break
                    if x in visited:
                        continue
                    visited.add(x)
                    for c,t in graph[x]:
                        que.append([c,total * t])
                if not found:
                    ans.append(-1)
        return ans