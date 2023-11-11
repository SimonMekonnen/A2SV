class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        
        
        visited = set()
        
        level = 0
        
        def change(mat):
            s = ""
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    s += str(mat[i][j])
            return s
        
        
        que = deque([mat])
        dire = [[0,1],[1,0],[-1,0],[0,-1]]
        while que:
            size = len(que)
          
            for i in range(size):
                cur = que.popleft()
                t = change(cur)
                if '0' in t and len(set(t)) == 1:
                    return level
                if t in visited:
                    continue

                visited.add(t)
    
                for i in range(len(cur)):
    
                    for j in range(len(cur[0])):
                        
                        now = copy.deepcopy(cur)
    
                        now[i][j] = 1 - now[i][j]
                   
                        for x,y in dire:
                            newx = x + i
                            newy = y + j
                            
                            if 0 <= newx < len(mat) and 0 <= newy < len(mat[0]):
                                now[newx][newy] = 1 - now[newx][newy]
                      
                        que.append(now)
            
           
            level += 1
        
        return -1
                
                
                                
                        
                
                
        