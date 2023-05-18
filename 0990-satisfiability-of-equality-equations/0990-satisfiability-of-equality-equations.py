class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equal = [i for i in range(26)]
        flag = True
        
        def findequal(c):
            return equal[ord(c) - ord('a')]

        
        def union(s):
            nonlocal flag
            parents1 = findequal(s[0])
            parents2 = findequal(s[-1])
            if s[1] == "!":
                if parents1 == parents2:
                    flag = False
    
            elif parents2 > parents1:
                for i in range(len(equal)):
                    if equal[i] == parents2:
                        equal[i] = parents1
            else:
                for i in range(len(equal)):
                    if equal[i] == parents1:
                        equal[i] = parents2
                    
        
        for i in equations:
            if i[1] == "=":
                union(i)
        for i in equations:
            if i[1] == "!":
                union(i)
 
        return flag
            
            
        
       
                

        
        