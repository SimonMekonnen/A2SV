class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic = defaultdict(lambda : 0)
        l = 0
        r = 10 
        while r <= len(s):
            dic[s[l:r]]+=1
            l+=1
            r+=1
        return [key for key,val in dic.items() if val > 1]
        
      
        
            
        