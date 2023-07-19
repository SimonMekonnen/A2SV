class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        dirs = [(0, 1), (1, 0)]
        inbound = lambda x, y : 0 <= x < n and 0 <= y < m
    
        dp = [[float('-inf') for _ in range(m + 1)] for _ in range(n + 1)]
        dp[n - 1][m - 1] = dungeon[-1][-1]
        # print('dd', dp)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i == n - 1 and j == m - 1:
                    continue
                dp[i][j] = min(dungeon[i][j], dungeon[i][j] + max(dp[i + 1][j], dp[i][j + 1]))
#         def dp(row, col):
                
#             if not inbound(row, col):
#                 return float('-inf')
#             if memo[row][col] != float('-inf'):
#                 return memo[row][col]
#             if row == n - 1 and col == m - 1:
#                 return dungeon[row][col]
            
#             memo[row][col] =  min(dungeon[row][col], dungeon[row][col] + max(dp(row + 1, col), dp(row, col + 1)))
#             return memo[row][col]
#         res = dp(0, 0)
        # print(dp)
        return abs(dp[0][0]) + 1 if dp[0][0] <= 0 else 1
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