class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        index = [i for i in range(len(tasks))]
        
        index.sort(key  = lambda x : tasks[x])
        ans = []
        heap = []
        tobe = 0
        while tobe < len(tasks):
            if heap:
                cur = heappop(heap)
                ans.append(cur[1])
                first += cur[0]
                while tobe < len(tasks) and tasks[index[tobe]][0] <= first:
                    heappush(heap,(tasks[index[tobe]][1],index[tobe]))
                    tobe += 1
            else:
                first = tasks[index[tobe]][0]
                while tobe < len(tasks) and tasks[index[tobe]][0] <= first:
                    heappush(heap,(tasks[index[tobe]][1],index[tobe]))
                    tobe += 1
                    
                
        while heap:
            ans.append(heappop(heap)[1])
        return ans
            
        
        