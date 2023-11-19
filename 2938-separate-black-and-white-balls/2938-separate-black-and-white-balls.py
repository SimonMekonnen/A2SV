class Solution:
    def minimumSteps(self, s: str) -> int:
        
        
        prev = 0
        count = 0
        for i in s:
            if i == '1':
                prev += 1
            else:
                count += prev
             
        return count
        