class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def helper(n):
            
            if n == 1:
                
                return "0"
            
            prev = helper(n - 1)
            
            now = [ "0" if i == "1" else "1" for i in prev]
            now.reverse()
            
            return prev + "1" + "".join(now)
        
        return helper(n)[k - 1]
            
        