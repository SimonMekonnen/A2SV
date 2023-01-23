class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        dire = [0,1]
        
        ans = set()
        ano = []
        row = 0
        col = 0
       
        while len(ans) < len(matrix) * len(matrix[0]):
            
            if (row + dire[0],col + dire[1]) in ans:
                dire[0] *= -1
                dire.reverse()
            elif  (col + dire[1] >= len(matrix[0])):
                dire[0] *= -1
                dire.reverse()
            elif  (row + dire[0]>= len(matrix)):
                dire[0] *= -1
                dire.reverse()
            elif (col + dire[1] < 0):
                dire[0] *= -1
                dire.reverse()
                
            
                
            if len(ans) == 0:
                ans.add((row,col))
                ano.append((row,col))
                
            row+=dire[0]
            col+=dire[1]
            ans.add((row ,col))
            ano.append((row,col))
        
        while len(ano) >  len(matrix) * len(matrix[0]):
            ano.pop()
        for i in range(len(ano)):
            ano[i] = matrix[ano[i][0]][ano[i][1]]
        
        return ano
                
                
            
            
        
        
        
                    
                    
                    
                    
            
            
            
            
        
      
    
        