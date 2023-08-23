class Solution:
    def minimumSum(self, n: int, k: int) -> int:
    
        avoid = set()
        count = 0
        ans = 0
        for i in range(1,k//2):     
            avoid.add(k - i)
        if k % 2 == 1:
            if (k - k//2 != k):
                avoid.add(k - (k//2))
        i = 1
        while count != n:
            if i not in avoid:
                count += 1
                ans += i
            i += 1
        return ans
            
            
            
        
        
        
     
       