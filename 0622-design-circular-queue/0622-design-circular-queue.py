class ListNode():
    def __init__ (self,val = 0,next = None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.que = ListNode()
        self.head = self.que
        self.tail = self.que
        self.size = k
        self.count = 0

    def enQueue(self, value: int) -> bool:
        newNode = ListNode(val = value)
        if self.count == 0:
            self.head = newNode
            self.tail = newNode
            self.count += 1
            return True
        elif self.count < self.size:
            self.tail.next = newNode
            self.tail = newNode
            self.count += 1
            return True
        
        return False
        
        
            
        

    def deQueue(self) -> bool:
        if self.count > 0:
            self.head = self.head.next
            self.count -= 1
            return True
        else:
            return False
    def Front(self) -> int:
        if self.count <= 0:
            return -1
        return self.head.val
        

    def Rear(self) -> int:
        if self.count <= 0:
            return -1
        return self.tail.val
        

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()