class Solution:
    def isToeplitzMatrix(self, m):
        for i in range(len(m) - 1):
            for j in range(len(m[0]) - 1):
                if m[i][j] != m[i + 1][j + 1]:
                    return False
        return True
    # [[36,59,71,15,26,82,87],
    #  [56,36,59,71,15,26,82],
    #  [15,0,36,59,71,15,26]]
   
            
        