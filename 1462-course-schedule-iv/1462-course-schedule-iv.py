class Solution:
    def checkIfPrerequisite(self, c: int, p: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for i in range(c)]
        degree = [0 for i in range(c)]
    
        for x,y in p:
            degree[y] += 1
            graph[x].append(y)
         
    
        que = deque()
        for i in range(len(degree)):
            if degree[i] == 0:
                que.append(i)
        
        ans = []
        while que:
            now = que.popleft()
            ans.append(now)
            for neigh in graph[now]:
                degree[neigh] -= 1
                if degree[neigh] == 0:
                    que.append(neigh)
        myanswer = [set() for i in range(c)]
        for i in range(len(ans)):
            for neigh in graph[ans[i]]:
                now = myanswer[ans[i]]
                for j in now:
                    myanswer[neigh].add(j)
                myanswer[neigh].add(ans[i])
        ans = []
        for x,y in queries:
            ans.append(x in myanswer[y])
        return ans
            
                
        
        
        