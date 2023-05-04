class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dic = defaultdict(set)
        for i in dislikes:
            dic[i[0]].add(i[1])
            dic[i[1]].add(i[0])
        visited = set()
        for i in range(1,n + 1):
            color = [2 for i in range(n + 1)]
            stk = [[i,1]]
            visited.add((i,1))
            while stk:
                now = stk.pop()
                if color[now[0]] != 2:
                    return False
                color[now[0]] = now[1]
                for i in dic[now[0]]:
                    if (i,1 - now[1]) not in visited:
                        stk.append([i,1 - now[1]])
                        visited.add((i,1 - now[1]))
        return True
                
                
        
        
                        
                        
            
            
        
        