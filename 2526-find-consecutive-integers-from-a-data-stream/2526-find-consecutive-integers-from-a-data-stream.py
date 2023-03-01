class DataStream:

    def __init__(self, value: int, k: int):
        self.dic = defaultdict(int)  
        self.val = value
        self.length = k
        self.arr = []
        self.right = 0
        self.left = 0
    def consec(self, num: int) -> bool:
        self.arr.append(num)
        if self.right - self.left + 1 <= self.length:
            self.right += 1 
            self.dic[num] += 1
            if len(self.dic) == 1 and self.dic[self.val] == self.length:
                return True
        else:
            self.dic[self.arr[self.left]] -= 1
            if self.dic[self.arr[self.left]] ==  0:
                 del self.dic[self.arr[self.left]]

            self.dic[num] += 1
            self.left += 1
            self.right += 1
            if len(self.dic) == 1 and self.val in self.dic:
                return True
    
                
            
            
    
        
    

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)