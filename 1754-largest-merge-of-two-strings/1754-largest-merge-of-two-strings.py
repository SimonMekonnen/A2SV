class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        a = 0
        b = 0
        ans = ""
        while a < len(word1) and b < len(word2):
                if word1[a : ] > word2[b : ]:
                    ans += word1[a]
                    a += 1
                else:
                    ans += word2[b]
                    b += 1
        ans += word1[a:]
        ans += word2[b : ]
        return ans
                    
                    
            
        
        