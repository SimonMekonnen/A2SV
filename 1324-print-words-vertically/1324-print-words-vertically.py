class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        n = max(s,key = lambda x : len(x))
        words = []
        for col in range(len(n)):
            word = ""
            
            for row in range(len(s)):
                
                if col < len(s[row]):
                    word+= s[row][col]
                else:
                    word+= " "
            
            words.append(word.rstrip())
        
        return words
        
        