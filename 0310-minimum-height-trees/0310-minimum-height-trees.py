class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1:
            return [0]
        graph = defaultdict(set)
        count = [0 for i in range(n)]
        for x,y in edges:
            graph[x].add(y)
            graph[y].add(x)
            count[x] += 1
            count[y] += 1
        
        que = deque()
        for i in range(len(count)):
            if count[i] == 1:
                que.append(i)

        while que:
            size = len(que)
            ans = []
            for _ in range(size):
                cur = que.popleft()
                ans.append(cur)
                for neigh in graph[cur]:
                    count[neigh] -= 1
                    if count[neigh] == 1:
                        que.append(neigh)
                    
        return ans