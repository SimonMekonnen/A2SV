class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        ans = []
        
        word = [Counter(i) for i in words]
    
        for i in word[0]:
            c = word[0][i]
            for j in range(1,len(word)):
                if i in word[j]:
                    
                    c = min(c,word[j][i])
                else:
                    c = 0
                    break
            ans += [i] * c
        
        return ans
       
            
            
        