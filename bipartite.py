from collections import deque


while True:
    n = int(input())
    if not n: break
    e = int(input())
    graph = [[] for i in range(n)]
    for i in range(e):
        x,y = list(map(int,input().split()))
        graph[x - 1].append(y - 1)
        graph[y - 1].append(x - 1)

    pos = 1
    que = deque()
    color = [0 for i in range(n)]
    vistied = [0 for i in range(n)]
    que.append([1,0])
    while que:
            cur = que.popleft()
            if vistied[cur[0]] : continue
            vistied[cur[0]] = 1
            color[cur[0]] = cur[1]
            for neigh in graph[cur[0]]:
                if vistied[neigh] == 0:
                    que.append([neigh,1 - cur[1]])
                else:
                    if color[neigh] == cur[1]:
                        pos = 0
    if pos:
        print('BICOLOURABLE.')
    else:
        print('NOT BICOLOURABLE.')
        
