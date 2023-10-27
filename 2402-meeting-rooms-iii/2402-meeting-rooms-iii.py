class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        

        ans = [[0,i,0] for i in range(n)]
        meetings.sort()
        heapify(ans)
        for x,y in meetings:
            arr = []
            while ans and ans[0][0] <= x:
                end,i,sofar = heappop(ans)
                arr.append([end,i,sofar])
            if arr:
                arr.sort(key = lambda x : x[1])
                arr[0][0] = y
                arr[0][2] += 1
                for i in arr:
                    heappush(ans,i)
            else:
                end,i,sofar = heappop(ans)
                heappush(ans,[y + end - x,i,sofar + 1])
                       
        t = 0
        for x,y,z in ans:
            t = max(t,z)
        ans.sort(key = lambda x : x[1])
        for x,y,z in ans:
            if z == t:
                return y
        