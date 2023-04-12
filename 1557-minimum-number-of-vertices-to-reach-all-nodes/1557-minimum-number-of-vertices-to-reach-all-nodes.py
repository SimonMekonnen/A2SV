class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        possible = set()
        np = set()
        
        for i in edges:
            
            possible.add(i[0])
            np.add(i[1])
        
        ans = []
        for i in possible:
            if i not in np:
                ans.append(i)
        
        return ans
            
        