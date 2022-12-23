class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        dic = {}
        for i in range(len(order)):
            dic[order[i]] = i
        
        for h in range(1,len(words)):
            p1 = 0
            Flag = True
            while p1 < len(words[h]) and p1 < len(words[h - 1]):
                if dic[words[h - 1][p1]] > dic[words[h][p1]]:
                    return False
                if dic[words[h - 1][p1]] < dic[words[h][p1]]:
                    Flag = False
                    break
                p1+=1
                
            if Flag and len(words[h - 1]) > len(words[h]):
                return False
        return True
                    
            
     
                
                
                
        
      
        