class Solution:
    def compress(self, chars: List[str]) -> int:
        c = len(chars)
        left,right = 0 , 0
        
        while right < c:
            current = chars[right]
            count = 0
            while right < c and chars[right] == current:
                
                right += 1
                count += 1
            
            chars[left] = current
            left+=1
            ch = str(count)
            if int(ch)!= 1:
                for i in ch:
                    chars[left] = i
                    left+=1

        
        return left
            
            
