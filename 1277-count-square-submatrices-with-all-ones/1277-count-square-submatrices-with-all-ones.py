class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    dia = 0
                    left = 0
                    up = 0
                    if row - 1 >= 0 and col - 1 >= 0:
                        dia = matrix[row - 1][col - 1]
                    if row - 1 >= 0:
                        up = matrix[row - 1][col]
                    if col - 1 >= 0:
                        left = matrix[row][col - 1]
                    
                    matrix[row][col] += min(dia,left,up) 
                    ans += matrix[row][col]
        return ans
                    