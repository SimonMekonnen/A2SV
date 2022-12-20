class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = -1
        for row in range(len(grid) - 2):
            for co1 in range(len(grid[0]) - 2):
                top = grid[row][co1] + grid[row][co1 + 1] + grid[row][co1 + 2]
                bottom = grid[row+2][co1] + grid[row + 2][co1 + 1] + grid[row + 2][co1 + 2]
                total = top + bottom + grid[row + 1][co1 + 1]
                ans = max(total , ans)
        return ans
        