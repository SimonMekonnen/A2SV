class DataStream:

    def __init__(self, value: int, k: int):
        self.stk = deque()
        self.val = value
        self.k = k

    def consec(self, num: int) -> bool:
        
        if num != self.val:
            self.stk = deque()
            return False
        self.stk.append(num)
        if len(self.stk) >= self.k:
            return True
        
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)