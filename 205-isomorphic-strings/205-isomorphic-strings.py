class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        another = {}
        for i in range(len(s)):
            if t[i] in dic:
                if dic[t[i]] != s[i]:
                    return False
            if s[i] in another:
                if another[s[i]] != t[i]:
                    return False
            dic[t[i]] = s[i]
            another[s[i]] = t[i]
    
        return True
                
 
        