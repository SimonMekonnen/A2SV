class MyQueue:
    def __init__(self):
        self.que=[]
    def push(self, x):
        self.que.append(x)
    def pop(self):
        return self.que.pop(0)
    def peek(self):
        return self.que[0]
    def empty(self):
        if len(self.que)==0:
             return True
        return False