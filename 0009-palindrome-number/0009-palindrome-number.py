class Solution:
    def isPalindrome(self, x: int) -> bool:
        c = x
        ans = []
        if c == 0:
            return True
        while c >= 1 :
            ans.append(c%10)
            c//=10
        if not ans:
            return False
        left = 0
        right = len(ans) - 1
        while left < right:
            if ans[left]!= ans[right]:
                return False
            left+=1
            right-=1
        return True
            
            
            
            
        
        
        
        