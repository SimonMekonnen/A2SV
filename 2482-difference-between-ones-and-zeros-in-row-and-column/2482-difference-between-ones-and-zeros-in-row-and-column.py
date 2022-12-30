class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row = []
        col = []
        for r in range(len(grid)):
            a = 0
            for c in range(len(grid[0])):
                a += grid[r][c] == 1
                a -= grid[r][c] == 0
            row.append(a)
        for c in range(len(grid[0])):
            a = 0
            for r in range(len(grid)):
                a += grid[r][c] == 1
                a -= grid[r][c] == 0
            col.append(a)
        ans = []
        for r in row:
            cc = []
            for c in col:
                cc.append(r + c)
            ans.append(cc)
        return ans
        
         
        