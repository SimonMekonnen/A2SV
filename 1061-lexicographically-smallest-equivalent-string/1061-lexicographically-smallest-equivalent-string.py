class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        parent  = [i for i in range(26)]

        def find(c):
            return parent[ord(c) - ord('a')]
        
        def union(s1,s2):
            parents1 = find(s1)
            parents2 = find(s2)
    
            for i in range(len(parent)):
                if parent[i] == parents1:
                    parent[i] = parents2
        
        i = 0
        while i < len(s1) and i < len(s2):
            union(s1[i],s2[i])
            i += 1
        
        ans = ""
        for i in baseStr:
            for j in range(26):
                if find(i) == parent[j]:
                    ans += chr(ord("a") + j)
                    break 
        
        return ans
                    
    
        