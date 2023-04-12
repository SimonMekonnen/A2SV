class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        possible = set()
        np = set()
        
        for i in edges:
            if i[1] in possible:
                possible.remove(i[1])
            if i[0] not in np:
                possible.add(i[0])
            np.add(i[1])
        
        return possible
            
        