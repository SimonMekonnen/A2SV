class MinStack:

    def __init__(self):
        self.stk = []  
    def push(self, val):
        c = self.getMin()
        if c == None or val < c:
            c = val
        self.stk.append((val,c))
    def pop(self):
        self.stk.pop()
    def top(self) -> int:
        return self.stk[-1][0]
    def getMin(self) -> int:
        if len(self.stk)==0:
            return None
        return self.stk[-1][1]
    
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()