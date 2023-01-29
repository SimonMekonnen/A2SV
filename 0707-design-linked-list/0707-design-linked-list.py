class node:
    
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next
    

class MyLinkedList:
    

    def __init__(self):
        self.node = node()
        self.head = None
    def get(self, index: int) -> int:
        
    
        current = self.head
        for i in range(index):
            if current == None:
                break
            current = current.next
        
        return current.val if current else -1 
        

    def addAtHead(self, val: int) -> None:
        
        new = node(val)
        if self.head == None:
            self.node = new
            self.head = new
        
        else:
            new.next = self.head
            self.head = new
        curr = self.head
       
        

    
    def addAtTail(self, val: int) -> None:
        
        new = node(val)
        if self.head == None:
            self.node = new
            self.head = new
        else:
        
            curr = self.head

            while curr and curr.next:

                curr = curr.next
        
        
            curr.next = new
        
        
        curr = self.head
        
        
        
    
        
        
        
            
        
        
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        dummy = node()
        dummy.next = self.head
        current = dummy
    
        new = node(val)
        if dummy.next != None:
            for i in range(index):

                current = current.next
            if current:
                new.next = current.next
                current.next = new
        else:
            if index == 0:
                dummy.next = new
            

        self.head = dummy.next
       
      
        

    def deleteAtIndex(self, index: int) -> None:
        dummy = node()
        dummy.next = self.head
        current = dummy
        if dummy.next != None:
            for i in range(index):

                current = current.next
            if current and current.next!=None:
                current.next = current.next.next
        
        self.head = dummy.next
        
        curr = self.head
      
        
        
    
        
        
        
   
    
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)