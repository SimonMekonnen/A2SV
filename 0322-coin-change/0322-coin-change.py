class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        que = deque([0])
        level = 0
        visited = set()
        while que:
            size = len(que)
            for i in range(size):
                cur = que.popleft()
                if cur == amount:
                    return level
                for i in range(len(coins)):
                    if cur + coins[i] <= amount and (cur + coins[i] , i) not in visited:
                        que.append(cur + coins[i])
                        visited.add((cur + coins[i] , i))
        
            level += 1
        return -1
                
        