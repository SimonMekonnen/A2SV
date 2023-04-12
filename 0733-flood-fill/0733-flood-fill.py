class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        visited = set()
        inital = image[sr][sc]
        def dfs(sr,sc,):
            if (sr,sc) in visited or sr >= len(image) or sr < 0  or sc < 0 or sc >= len(image[0]) or image[sr][sc] != inital:
                return 
            
            image[sr][sc] = color
            visited.add((sr,sc))
            dfs(sr - 1,sc)
            dfs(sr + 1,sc)
            dfs(sr ,sc + 1)
            dfs(sr,sc - 1)
        dfs(sr,sc)
        return image
        
        
        