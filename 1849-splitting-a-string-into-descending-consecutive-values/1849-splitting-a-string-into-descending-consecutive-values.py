class Solution:
    def splitString(self, s: str) -> bool:
        stk = []
        def helper(end):
            
            if end >= len(s):
                return len(stk) >= 2
        
          
            for i in range(end,len(s)):
                if not stk or (int(stk[-1]) - int(s[end : i + 1]))== 1:
                    stk.append(s[end : i + 1])
                    if helper(i + 1):
                        return True
                    stk.pop()
            return False
        
        return helper(0)
                
                
                
                
        