class Solution:
    def maximumRobots(self, charge: List[int], cost: List[int], k: int) -> int:
        
        
        left  = 0
        stk = deque()
        total = 0
        ans = 0
        for right in range(len(cost)):
            total += cost[right]
            while stk and charge[right] > charge[stk[-1]]:
                stk.pop()
            
            stk.append(right)
            
            while stk and left <= right and charge[stk[0]] + (right - left + 1) * total > k:
                total -= cost[left]
                if stk[0] == left:
                    stk.popleft()
                
                left += 1
                
            if stk:
                ans = max(right - left + 1,ans)
            
        return ans
            
            
        
        
        
        