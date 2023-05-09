class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.graph[kingName] = []
        self.first = kingName
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
        self.graph[childName] = []
   

    def death(self, name: str) -> None:
        self.dead.add(name)
        return None

    def getInheritanceOrder(self) -> List[str]:
        stk = [self.first]
        visited = set([self.first])
        ans = []
        while stk:
            cur = stk.pop()
            if cur not in self.dead:
                ans.append(cur)
            for i in self.graph[cur][::-1]:
                if i not in visited:
                    stk.append(i)
                    visited.add(i)            
        return ans
        
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()