class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        dest = set()
        direction = [(0,1),(1,0),(-1,0),(0,-1)]

        for row in range(len(maze)):
            for col in range(len(maze[0])):
                if (row == 0 or col == 0 or row == len(maze) - 1 or col == len(maze[0]) - 1) and maze[row][col] == "." and [row,col] != entrance:
                    dest.add((row,col))
        
        que = deque([entrance])
        count = 0
        visited = set()
        visited.add(tuple(entrance))
        while que:
            size = len(que)
            for _ in range(size):
                x,y = que.popleft()
                if (x,y) in dest:
                    return count
                for X,Y in direction:
                    newx = X + x
                    newy = Y + y
                    if 0 <= newx < len(maze) and 0 <= newy < len(maze[0]) and maze[newx][newy] == ".":
                        if (newx,newy) not in visited:
                            que.append([newx,newy])
                            visited.add((newx,newy))
            count += 1
        return -1
            
                
            
        
        
                    
        
        
        