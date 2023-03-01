class Node():
    def __init__(self,val = 0 , next = None):
        self.val = val
        self.next = next
class MyCircularDeque:

    def __init__(self, k: int):
        self.now = Node()
        self.head = self.now
        self.tail = self.now
        self.size = k
        self.length = 0

    def insertFront(self, value: int) -> bool:
        if self.size <= self.length:
            return False
        
        new = Node(val = value)
        new.next = self.head
        self.head = new
        self.length += 1
        curr = self.head
        if self.length == 1:
            self.tail = self.head
        return True

    def insertLast(self, value: int) -> bool:
        if self.size <= self.length:
            return False
        new = Node(val = value)
        self.tail.next = new
        self.tail = new
        self.length += 1
        if self.length == 1:
            self.head = self.tail
    
        return True


    def deleteFront(self) -> bool: 
        if self.length <= 0 :
            return False
        dummy = Node()
        dummy.next = self.head.next
        self.head =dummy.next
        self.length -= 1
        return True

    def deleteLast(self) -> bool:
        if self.length <= 0 :
            return False
        dummy = Node()
        dummy.next = self.head
        curr = dummy
        last = dummy.next
        
        while last != self.tail:
            curr = curr.next
            last = last.next
        curr.next = None
        self.tail = curr
        self.length -= 1
        return True
    def getFront(self) -> int:
        return self.head.val if self.length > 0 else -1

    def getRear(self) -> int:
        
        return self.tail.val if self.length > 0 else -1 
    def isEmpty(self) -> bool:
        
        return self.length == 0
    def isFull(self) -> bool:
        return self.length == self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()