class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        ans = []
        for x,y,r in queries:
            count = 0
            for x1,y1 in points:
                now = (x1 - x)**2 + (y1 - y)**2
                if now <= r**2:
                    count += 1
            ans.append(count)
        return ans
        