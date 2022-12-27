class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], ar: int) -> int:
        
        for r,c in enumerate(rocks):
            rocks[r] = capacity[r] - c
        
        rocks.sort()
        ans = 0
        i = 0
        while ar >= 0 and i < len(rocks):
            
            if rocks[i] <= ar:
                ans+=1
                
            ar -= rocks[i]
            i+=1
        
        return ans
            
        
        
        
        
    
        