class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        que = deque([0])
        
        while que:
            now = que.popleft()
            visited.add(now)
            for i in rooms[now]:
                if i not in visited:
                    que.append(i)
        return len(visited) == len(rooms)