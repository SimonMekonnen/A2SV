class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dic = {}
        left = 0
        count = 0
        
        for right in range(len(s)):
            dic[s[right]] = dic.get(s[right],0)+1
        
            while len(dic) >= 3:
                count += len(s)-right
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    del dic[s[left]]
                left += 1
        
        return count
                
                      