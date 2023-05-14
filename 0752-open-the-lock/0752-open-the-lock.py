class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        
    
        dead = set(deadends)
        que = deque(["0000"])
        if "0000" in dead:
            return -1
        level = 0
        visited = set()
        visited.add("0000")
 
        graph = {0 : {1,9},
                 1 : {2,0},
                 2 : {1,3},
                 3 : {4,2},
                 4 : {3,5},
                 5 : {4,6},
                 6: {5,7},
                 8 : {7,9},
                 7 : {6,8},
                 9 : {8,0},}
        while que:
            size = len(que)
            for _ in range(size):
                cur = list(que.popleft())
                if "".join(cur) == target:
                    return level
                
                for i in range(4):
                     c = cur.copy()
                     for j in graph[int(c[i])]:
                        c[i] = str(j)
                        now = "".join(c)
                        if now not in visited and now not in dead :
                                que.append(now)
                                visited.add(now)
                            
            level += 1
        
        return -1
                    
                    
                    
                   
                    
                    
                    
                
            
        
        
        