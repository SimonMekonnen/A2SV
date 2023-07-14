class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.graph = [[] for i in range(len(parent))]
        for i in range(len(parent)):
            if parent[i] != -1:
                self.graph[parent[i]].append(i)
        self.locked = [-1 for i in range(len(parent))]
        
    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] == -1 :
            self.locked[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] == user:
            self.locked[num] = -1
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        
        temp = num
        while temp != -1:
            if self.locked[temp] != -1:
                
                return False
            temp = self.parent[temp]
        
        def dfs(node, unlock):
           
            if not unlock:
                flag = 0
                for neigh in self.graph[node]:
                    flag |= self.locked[neigh] != -1 or dfs(neigh, unlock)
                
                return flag
            
            else:
                for neigh in self.graph[node]:
                    dfs(neigh, unlock)
                self.locked[node] = -1
        
        
        
        if dfs(num, False):
            
            dfs(num, True)
            self.locked[num] = user
            return True
        return False
            
            
            
           
            
            
        
        
        
        
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)