"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importa = {}
        subs = {}
        for i in employees:
            importa[i.id] = i.importance
            subs[i.id] = i.subordinates
        
        que = deque([id])
        count = 0
        while que:
            s = len(que)
            for i in range(s):
                now = que.popleft()
                count += importa[now]
                sub = subs[now]
                que.extend(sub)
   
        return count
        