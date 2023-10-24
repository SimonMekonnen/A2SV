class Solution:
    def canBeTypedWords(self, text: str, b: str) -> int:
        
        
        text = text.split()
        
        ans = 0
        for i in text:
            pos = 0
            for j in i:
                if j in b:
                    pos = 1
            if pos:
                ans += 1
        return len(text) - ans 
        