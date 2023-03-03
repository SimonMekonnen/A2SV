class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        
        while left <= right:
            mid = (right + left)//2
            time = 0
            
            for i in piles:
                time += ceil(i / mid)
                
            if time > h:
                left = mid + 1
            
            else:
                right = mid - 1
                
        return left
                
                
                
        
        
        