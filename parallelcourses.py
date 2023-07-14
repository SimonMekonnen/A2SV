from collections import deque
def parallelCourses(n, prerequisites):
    graph = [[] for i in range(n)]
    degree = [0 for i in range(n)]
    for x,y in prerequisites:
        graph[x - 1].append(y - 1)
        degree[y - 1] += 1
    que = deque()
    for i in range(len(degree)):
        if degree[i] == 0:
            que.append(i)
    
    count = 0
    ans = []
    while que:
        size = len(que)
        for i in range(size):
            cur = que.popleft()
            ans.append(cur)
            for neigh in graph[cur]:
                degree[neigh] -= 1
                if degree[neigh] == 0:
                    que.append(neigh)
        count += 1
    if len(ans) == n:
        return count
    else:
        return -1
