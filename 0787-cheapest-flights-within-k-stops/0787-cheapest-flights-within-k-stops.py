class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ans = [inf for i in range(n)]
        ans[src] = 0
        for i in range(k + 1):
            newarr = [inf for i in range(n)]
            newarr[src] = 0
            for x,y,w in flights:
                newarr[y] = min(ans[x] + w,newarr[y])
            ans = newarr
        return ans[dst] if ans[dst] != inf else -1
        