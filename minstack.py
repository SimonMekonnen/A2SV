class MinStack:
    def __init__(self):
        self.stk = []
    def push(self, val):
        self.stk.append(val)
    def pop(self):
        self.stk.pop()
    def top(self) -> int:
        return self.stk[-1]
    def getMin(self) -> int:
        return min(self.stk)