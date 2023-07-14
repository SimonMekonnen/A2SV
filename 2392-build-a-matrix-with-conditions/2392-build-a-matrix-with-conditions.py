class Solution:
    def buildMatrix(self, k: int, rowc: List[List[int]], colc: List[List[int]]) -> List[List[int]]:
        
        row  = [[] for i in range(k)]
        col = [[] for i in range(k)]
        rdegree = [0 for i in range(k)]
        cdegree = [0 for i in range(k)]
        for x,y in rowc:
            row[x - 1].append(y - 1)
            rdegree[y - 1] += 1
        
        for x,y in colc:
            col[x - 1].append(y - 1)
            cdegree[y - 1] += 1
        
        que = deque()
        for i in range(k):
            if rdegree[i] == 0:
                que.append(i)
        
        rorder = {}
        while que:
            cur = que.popleft()
            rorder[cur + 1] = len(rorder)
            for neigh in row[cur]:
                rdegree[neigh] -= 1
                if not rdegree[neigh]:
                    que.append(neigh)
        corder = {}
        que = deque()
        for i in range(k):
            if cdegree[i] == 0:
                que.append(i)
        while que:
            cur = que.popleft()
            corder[cur + 1] = len(corder)
            for neigh in col[cur]:
                cdegree[neigh] -= 1
                if not cdegree[neigh]:
                    que.append(neigh)
        if len(rorder) != len(corder) or len(rorder) != k or len(corder) != k:
            return []
        
        ans = [[0 for i in range(k)] for i in range(k)]

        for i in rorder:
            r = rorder[i]
            c = corder[i]
            ans[r][c] = i
        return ans
        
        
        
            
        
        