class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        dirs = [(0, 1), (1, 0)]
        inbound = lambda x, y : 0 <= x < n and 0 <= y < m
        @cache
        def dp(row, col):
            if not inbound(row, col):
                return float('-inf')
            if row == n - 1 and col == m - 1:
                return dungeon[row][col]
            
            return min(dungeon[row][col], dungeon[row][col] + max(dp(row + 1, col), dp(row, col + 1)))
        res = dp(0, 0)
        return abs(res) + 1 if res <= 0 else 1
#         def good(health):
#             seen = set()
#             if health + dungeon[0][0] <= 0:
#                 return False
#             queue = deque([(0, 0, health + dungeon[0][0])])
            
#             while queue:
#                 curr_x, curr_y, curr_h = queue.popleft()
#                 if (curr_x, curr_y) == (n - 1, m - 1):
#                     return True
#                 for dx, dy in dirs:
#                     new_x, new_y = curr_x + dx, curr_y + dy
                    
#                     if inbound(new_x, new_y) and (new_x, new_y, curr_h + dungeon[new_x][new_y]) not in seen:
#                         if curr_h + dungeon[new_x][new_y] > 0:
#                             seen.add((new_x, new_y, curr_h + dungeon[new_x][new_y]))
#                             queue.append((new_x, new_y, curr_h + dungeon[new_x][new_y]))
#             return False
                
            
            
        
#         left, right = 0, 400001
#         while right > left + 1:
#             mid = left + (right - left) // 2
#             if good(mid):
#                 right = mid
#             else: left = mid
        
#         return right