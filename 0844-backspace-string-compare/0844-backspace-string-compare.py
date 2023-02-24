class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stack = []
        stack2 = []
        
        for i in s:
            if stack and i == "#":
                stack.pop()
                
            elif i != "#":
                stack.append(i)
          
        for i in t:
            if stack2 and i == "#":
                stack2.pop()
                
            elif i != "#":
                stack2.append(i)
 
        return stack == stack2
        