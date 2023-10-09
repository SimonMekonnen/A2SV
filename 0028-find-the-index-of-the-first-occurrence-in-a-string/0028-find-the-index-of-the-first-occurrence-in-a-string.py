class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        need = 0
        for i in needle:
            need *= 27
            need %= (10 ** 9 + 7)
            need += ord(i) - ord('a') + 1
            
        
        left = 0
        window = 0
        for right in range(len(haystack)):
            if right < len(needle):
                window *= 27
                window %= (10 ** 9 + 7)
                window += ord(haystack[right]) - ord('a') + 1
            else:
                if window == need:
                    return left
                window -= (ord(haystack[left]) - ord('a') + 1) * pow(27,right - left - 1,10**9 + 7)
                window *= 27
                window %= (10 ** 9 + 7)
                window += ord(haystack[right]) - ord('a') + 1
                left += 1
                
        return left if window == need else -1
                
            
       