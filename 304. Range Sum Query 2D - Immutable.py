class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        matrix.insert(0,[0]*(len(matrix[0])))
        for i in matrix:
            i.insert(0,0)
        self.pre = matrix
        row = 1
        while row < len(matrix):
            col = 1
            while col < len(matrix[0]):
                self.pre[row][col]+=self.pre[row][col-1]+self.pre[row-1][col] - self.pre[row - 1][col-1]
                col+=1
            row+=1  
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre[row2+1][col2+1] + self.pre[row1][col1] - self.pre[row1][col2+1] - self.pre[row2 + 1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)