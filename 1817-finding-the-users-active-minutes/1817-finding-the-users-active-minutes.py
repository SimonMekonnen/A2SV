class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        for i in range(len(logs)):
            logs[i] = tuple(logs[i])
        logs = set(logs)
        
        b = [i[0] for i in logs]
        c = Counter(b)
        ans = [0] * k
        for key, val in c.items():
            if val - 1 < len(ans):
                ans[val - 1] += 1
        return ans
        
        