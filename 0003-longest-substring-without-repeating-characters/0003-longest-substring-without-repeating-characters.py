class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic = {}
        left = 0
        maxx = float('-inf')
        
        for right in range(len(s)):
            
            while s[right] in dic:
                
                del dic[s[left]]
                left += 1
          
            dic[s[right]] = right
            maxx = max(maxx,right-left+1)
        return maxx if maxx != float('-inf') else 0
            
                
                
        
    
      
    