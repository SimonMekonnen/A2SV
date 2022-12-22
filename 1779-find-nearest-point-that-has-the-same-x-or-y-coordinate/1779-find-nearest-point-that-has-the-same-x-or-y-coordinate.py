class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        ans = -1
        cal = math.inf
        
        for i in range(len(points)):
            man = abs(x - points[i][0]) + abs(y - points[i][1])
            
            if (x ==  points[i][0] or y ==  points[i][1]) and man < cal:
                cal = man
                ans = i
                
        return ans
                
                
            
            
            
            
        