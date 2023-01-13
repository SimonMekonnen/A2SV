class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        swap = set()
        
        for row in range(len(matrix)):
            
            for col in range(len(matrix[0])):
                if (col,row) not in swap:
                    swap.add((row,col))


        for row,col in swap:
            matrix[row][col],matrix[col][row] = matrix[col][row], matrix[row][col]
        
        for row in range(len(matrix)):
            
            matrix[row].reverse()
            

            
           
                
                
        