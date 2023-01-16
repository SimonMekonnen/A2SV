class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if r * c != (len(mat) * len(mat[0])):
            
            return mat
        else:
            
            ans = [[0 for i in range(c)] for j in range(r) ]
            b = 0
            d = 0
            for row in range(len(mat)):
                
                for col in range(len(mat[0])):
                    
                    if d >= c:
                        d = 0
                        b+=1
                    ans[b][d] = mat[row][col]
                    d+=1
            
            return ans
        