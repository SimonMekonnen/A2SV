class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        if left:
            left = max(left)
        if right:
            right = min(right)
        if left == []:
            left = 0
        if right == []:
            right = n
        return max(n - right,left)
        
    
      
        
        
        
        