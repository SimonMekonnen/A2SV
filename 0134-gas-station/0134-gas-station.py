class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        c = len(gas)
        total = 0
        gas += gas
        left = 0
        cost += cost
        ans = -1
        for i in range(len(gas)):
            total += gas[i] 
            total -= cost[i]
            if total < 0:
                left = i + 1
                total = 0
            if i - left + 1 == c:
                ans = left
        
        return ans
                
            
            
            
        
        
        
        
        