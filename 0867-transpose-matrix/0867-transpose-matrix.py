class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = [[0 for n in matrix] for b in matrix[0]]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                ans[col][row] = matrix[row][col]
        return ans
       
      
        