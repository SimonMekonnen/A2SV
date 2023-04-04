class Solution:
    def maxProduct(self, words: List[str]) -> int:
      
        today = []
        for i in words:
            rep = ["0" for i in range(26)]
            for j in i:
                rep[ord(j) - ord("a")] = "1"

            today.append(int("".join(rep),2))
        ans = 0
        for i in range(len(words)):
            for j in range(i,len(words)):
                if today[i] & today[j] == 0:
                    ans = max(ans,len(words[i] * len(words[j])))
        return ans
        
            
        
        
        
      
        