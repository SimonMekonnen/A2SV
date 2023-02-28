class Solution:
    def simplifyPath(self, path: str) -> str:
        
        newpath = path.split("/")
        
        stk = []
        print(newpath)
        for i in newpath:
            if i == ".":
                pass
            elif i == "..":
                if stk:
                    stk.pop()
            else:
                if i != "":
                    stk.append(i)
        return "/" + "/".join(stk) if stk else "/"
                
        
        
        
        
        
    
        
   
        
        