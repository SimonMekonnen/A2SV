class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ans = ""
        
        for s in range(len(strs[0])):
            for r in range(1,len(strs)):
                if len(strs[r]) <= s or strs[0][s]!=strs[r][s]: 
                    return ans
            ans+=strs[0][s]
        return ans
            
    
        
        
     
                    
        
       
        
        