class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = -1
        _max = math.inf
        for k,i in enumerate(points):
            if i[1] == y or i[0] == x:
                b = abs(i[1] - y) + abs(i[0] - x) 
                if _max > b:
                    _max = b
                    ans = k
        return ans
                
                
                
        