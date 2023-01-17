class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        dire = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],[(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],[(0,0),(1,1),(2,2)],[(2,0),(1,1),(0,2)]]
        ans = 0
        for row in range(len(grid) - 2):
            
            for col in range(len(grid[0]) - 2):
                
                arr = set()
                di = set()
                for i in dire:
                    
                    total = 0
                    for j in i:
                        
                        if  10 > grid[row + j[0]][col + j[1]] > 0:
                            di.add(grid[row + j[0]][col + j[1]])
                        total+=(grid[row + j[0]][col + j[1]])
                    
                    arr.add(total)
        
                if len(arr) == 1 and len(di) == 9:
                    ans+=1
        return ans