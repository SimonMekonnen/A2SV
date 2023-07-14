class Solution:
    def sortItems(self, n: int, m: int, group: List[int], graph: List[List[int]]) -> List[int]:
        
        graph1 = [set() for i in range(n)]
        degree1 = [0 for i in range(n)]
        last = m 
        for i in range(len(group)):
            if group[i] == -1:
                group[i] = last
                last += 1
        graph2 = [set() for i in range(last)]
        degree2 = [0 for i in range(last)]
        dic = defaultdict(list)
        for i in range(len(graph)):
            
            for neigh in graph[i]:
                if group[i] == group[neigh]:
                    graph1[neigh].add(i)
                    degree1[i] += 1
                else:
                    if group[i] not in  graph2[group[neigh]]:
                        graph2[group[neigh]].add(group[i])
                        degree2[group[i]] += 1
        que = deque()
        for i in range(len(degree1)):
            if degree1[i] == 0:
                que.append(i)
        count = 0
        while que:
            cur = que.pop()
            dic[group[cur]].append(cur)
            count += 1
            for neigh in graph1[cur]:
                degree1[neigh] -= 1
                if not degree1[neigh]:
                    que.append(neigh)
        if count != n:
            return []
        que = deque()
        for i in range(len(degree2)):
            if degree2[i] == 0:
                que.append(i)
        order = []
        while que:
            cur = que.pop()
            order.append(cur)
            for neigh in graph2[cur]:
                degree2[neigh] -= 1
                if not degree2[neigh]:
                    que.append(neigh)
        
        if len(order) != last:
            return []
        
        ans = []
        for i in order:
            ans += dic[i]
        return ans
        
                    
        
            