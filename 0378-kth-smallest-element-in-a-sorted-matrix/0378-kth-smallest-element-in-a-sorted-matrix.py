class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        myarr = []
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if len(myarr) < k:
                    heappush(myarr,-matrix[row][col])
                else:
                    heappush(myarr,-matrix[row][col])
                    heappop(myarr)
        return -myarr[0]
                    