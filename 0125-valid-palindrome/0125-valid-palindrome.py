class Solution:
    def isPalindrome(self, s: str) -> bool:
        b=''.join(e for e in s if e.isalnum()).lower()
        i = 0
        j = len(b)-1
        while i < j:
            if b[i] != b[j]:
                return False
            i+=1
            j-=1
        return True
                
        
        