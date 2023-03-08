class Solution:
    def hIndex(self, c: List[int]) -> int:
        
        
        left = 0
        right = max(c)
        
        while left <= right:
              
            mid = (left + right)// 2
            t = bisect_left(c,mid)
         
            if mid > len(c) - t:
                right = mid - 1
            
            else:
                # if mid  == len(c) - t:
                ans = mid
                
                left = mid + 1
                
  
        return ans
                
            
        
            
            
            
            
            
        