class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        
        graph = defaultdict(set)
        depend = [0 for i in range(numCourses)]
        for d,i in pre:
            graph[i].add(d)
            depend[d] += 1
        
        que = deque()
        visited = set()
        for i,n in enumerate(depend):
            if n == 0:
                que.append(i)
                visited.add(i)
                
        

        while que:
            cur = que.popleft()
            visited.add(cur)
            for ne in graph[cur]:
                depend[ne] -= 1
                if depend[ne] == 0:
                    que.append(ne)
                    visited.add(ne)
        
        if len(visited) == numCourses:
            return True
        return False
            
                
        
    
        
        