class Solution:
    def shipWithinDays(self, w: List[int], days: int) -> int:
        
        left = max(w)
        right = sum(w)
        while left <= right:
            mid = (right + left)//2
            time = 1
            total = 0
            for i in w:
                total += i
                if total > mid:
                    time += 1
                    total = i
      
            if time > days:
                left = mid + 1
            
            else:
                right = mid - 1
                
        return left 
                
        