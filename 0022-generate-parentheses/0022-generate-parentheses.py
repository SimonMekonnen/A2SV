class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = set()
        dp.add("()")
        for i in range(2,n + 1):
            newdp = set()
            for j in dp:
                cur = 0
                newdp.add(j + "()")
                while cur < len(j):
                    t = len(j) - 1
                    if j[cur] == '(':
                        while t > cur:
                            if j[t] == ")":
                                now = list(j)
                                now.insert(cur,"(")
                                now.insert(t + 1,")")
                                newdp.add("".join(now))
                            t -= 1
                
                                
                    cur += 1
            dp = newdp
        return dp
        
            
            
        
        
        
        

        
        