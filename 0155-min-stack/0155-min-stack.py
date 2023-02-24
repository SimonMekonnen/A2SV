class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = 0
    def push(self, val: int) -> None:
        
        if len(self.stack) == 0:
            self.stack.append((val,self.mini))

        
        else:
            if val < self.stack[self.mini][0]:
                self.mini = len(self.stack)
            self.stack.append((val,self.mini))
    
    def pop(self) -> None:
        c = self.stack.pop()
        if self.stack:
            self.mini = self.stack[-1][1]
        else:
            self.mini = 0
            
        return c[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[self.stack[-1][1]][0]

        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()