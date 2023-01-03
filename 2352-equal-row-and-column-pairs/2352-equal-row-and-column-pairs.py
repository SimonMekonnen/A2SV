class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        dic = defaultdict(int)
        ans = 0
        for i in grid:
            dic[tuple(i)]+=1
        
        for col in range(len(grid[0])):
            c = []
            
            for row in range(len(grid)):
                
                c.append(grid[row][col])
                
            ans += dic[tuple(c)]
        
        return ans
                
                
                
        
        