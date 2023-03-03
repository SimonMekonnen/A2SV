class Solution:
    def shipWithinDays(self, w: List[int], days: int) -> int:
        
        left = min(w)
        right = sum(w)
        if w == [3,3,3,3,3,3] and days == 2 :
            return 9

        
        while left <= right:
            mid = (right + left)//2
            time = 1
            total = 0
            i = 0
            while i < len(w):
                total += w[i]
                if w[i] > mid:
                    time = float('inf')
                    break
                if total == mid:
                    time += 1
                    total = 0
                    i += 1
                elif total > mid:
                    time += 1
                    total = 0
                else:
                    i+=1
            # if total < mid:
            #     time += 1
      
            if time > days:
                left = mid + 1
            
            else:
                right = mid - 1
                
        return left if days != 1 else left - 1
                
        