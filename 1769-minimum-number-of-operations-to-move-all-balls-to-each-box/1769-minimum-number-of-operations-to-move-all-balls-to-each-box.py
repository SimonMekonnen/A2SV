class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        boxes = list(map(int,boxes))
        
        result = []
        
        for i in range(len(boxes)):
            ans = 0
            l = i
            r = len(boxes) - 1
             
            while l >= 0:
                
                ans+= (i - l) if boxes[l] == 1 else 0
                
                l-=1
                
            while r >= i:
                
                ans += (r - i) if boxes[r] == 1 else 0
                
                r-=1
                
            result.append(ans)
            
        return result
           
                
                
        