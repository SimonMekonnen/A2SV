class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        
        while i < len(haystack):   
            if haystack[i] != needle[j]:
                i = i - j + 1
                j = 0
    
            else:
                j += 1
                if j == len(needle):
                    return i - j + 1
                i += 1
        
        return -1