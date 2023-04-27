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
        count = 0
        def helper(id):
            nonlocal count
            count += importa[id]
            if not subs[id]:
                return 
            for i in subs[id]:
                helper(i)
                
        helper(id)
        return count
#        
        
#         def helper(id)
        
        