class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        ans = [inf for i in range(n)]
        graph = [[] for i in range(n)]
    
        ans[k - 1] = 0
        for i in range(n - 1):
            for x,y,w in times:
                ans[y - 1] = min(ans[y - 1], ans[x - 1] + w)
        return max(ans) if max(ans) != inf else -1