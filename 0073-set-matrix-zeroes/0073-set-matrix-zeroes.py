class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        """
        zrow = [0] * len(matrix)
        zcol = [0] * len(matrix[0])
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zrow[row] = 1
        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                if matrix[row][col] == 0:
                    zcol[col] = 1
        
        for row in range(len(matrix)):
            if zrow[row] == 1:
                for col in range(len(matrix[0])):
                    matrix[row][col] = 0

        for col in range(len(matrix[0])):
            if zcol[col] == 1:
                for row in range(len(matrix)):
                    matrix[row][col] = 0
                
        
        
        
                    
                

                
                
        